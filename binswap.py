import os
import sys
from pathlib import Path


class SimpleKeyEncoder:
    """
    Key-based encoder implementing XOR encryption with binary reversal.
    Supports both Base-4 and hexadecimal output formats.
    """
    
    def __init__(self, key: str):
        """
        Initialize encoder with encryption key.
        
        Args:
            key: Encryption key string
        """
        self.key = key
    
    def _extend_key(self, length: int) -> str:
        """
        Extend key to match required length through repetition.
        
        Args:
            length: Target length for extended key
            
        Returns:
            Extended key string
        """
        if not self.key:
            return '\x00' * length
        return (self.key * (length // len(self.key) + 1))[:length]
    
    def encode(self, text: str) -> str:
        """
        Encode text using XOR encryption and binary reversal to Base-4.
        
        Args:
            text: Plain text to encode
            
        Returns:
            Base-4 encoded string
        """
        extended_key = self._extend_key(len(text))
        xored = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, extended_key))
        binary = ''.join(format(ord(c), '08b')[::-1] for c in xored)
        
        base4 = ''
        for i in range(0, len(binary), 2):
            pair = binary[i:i+2]
            base4 += str(int(pair, 2))
        
        return base4
    
    def decode(self, encoded: str) -> str:
        """
        Decode Base-4 encoded text.
        
        Args:
            encoded: Base-4 encoded string
            
        Returns:
            Decoded plain text
        """
        binary = ''.join(format(int(digit), '02b') for digit in encoded)
        
        chars = []
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            reversed_byte = byte[::-1]
            chars.append(chr(int(reversed_byte, 2)))
        xored_text = ''.join(chars)
        
        extended_key = self._extend_key(len(xored_text))
        original = ''.join(chr(ord(x) ^ ord(k)) for x, k in zip(xored_text, extended_key))
        
        return original
    
    def encode_to_hex(self, text: str) -> str:
        """
        Encode text using XOR encryption and binary reversal to hexadecimal.
        
        Args:
            text: Plain text to encode
            
        Returns:
            Hexadecimal encoded string
        """
        extended_key = self._extend_key(len(text))
        xored = ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, extended_key))
        binary = ''.join(format(ord(c), '08b')[::-1] for c in xored)
        
        hex_str = ''
        for i in range(0, len(binary), 4):
            nibble = binary[i:i+4]
            hex_str += format(int(nibble, 2), 'x')
        
        return hex_str
    
    def decode_from_hex(self, encoded: str) -> str:
        """
        Decode hexadecimal encoded text.
        
        Args:
            encoded: Hexadecimal encoded string
            
        Returns:
            Decoded plain text
        """
        binary = ''.join(format(int(h, 16), '04b') for h in encoded)
        
        chars = []
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            reversed_byte = byte[::-1]
            chars.append(chr(int(reversed_byte, 2)))
        xored_text = ''.join(chars)
        
        extended_key = self._extend_key(len(xored_text))
        original = ''.join(chr(ord(x) ^ ord(k)) for x, k in zip(xored_text, extended_key))
        
        return original


class BinSwapTUI:
    """
    Text-based user interface for BinSwap encoder/decoder.
    Provides menu-driven interface for encoding and decoding operations.
    """
    
    def __init__(self):
        """Initialize TUI with empty encoder and key."""
        self.encoder = None
        self.key = None
    
    def clear_screen(self):
        """Clear terminal screen based on operating system."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Display application header with ASCII art logo."""
        print("\n" + "=" * 60)
        print("███████████████████████████████████████████████")
        print("█▄─▄─▀█▄─▄█▄─▀█▄─▄█─▄▄▄▄█▄─█▀▀▀█─▄██▀▄─██▄─▄▄─█")
        print("██─▄─▀██─███─█▄▀─██▄▄▄▄─██─█─█─█─███─▀─███─▄▄▄█")
        print("▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▀")
        print("\n        Simple Key-Based Encoder/Decoder")
        print("=" * 60 + "\n")
    
    def print_menu(self):
        """Display main menu options."""
        print("+--------------------------------------------------------+")
        print("|                      MAIN MENU                         |")
        print("+--------------------------------------------------------+")
        print("|  1. Encode Text                                        |")
        print("|  2. Decode Text                                        |")
        print("|  3. Encode File                                        |")
        print("|  4. Decode File                                        |")
        print("|  5. Change Key                                         |")
        print("|  6. Exit                                               |")
        print("+--------------------------------------------------------+\n")
    
    def get_key(self):
        """
        Prompt user for encryption key with confirmation.
        Validates non-empty key and ensures match on confirmation.
        """
        while True:
            key = input("Enter your encryption key: ").strip()
            if not key:
                print("ERROR: Key cannot be empty. Please try again.\n")
                continue
            
            confirm = input("Confirm your key: ").strip()
            if key != confirm:
                print("ERROR: Keys don't match. Please try again.\n")
                continue
            
            self.key = key
            self.encoder = SimpleKeyEncoder(key)
            print(f"SUCCESS: Key set successfully (Length: {len(key)} characters)\n")
            break
    
    def encode_text(self):
        """
        Handle text encoding operation.
        Prompts for input text and output format, displays encoded result.
        """
        print("\n" + "-" * 60)
        print("ENCODE TEXT")
        print("-" * 60)
        
        text = input("\nEnter text to encode (or 'back' to return): ").strip()
        if text.lower() == 'back':
            return
        
        if not text:
            print("ERROR: Text cannot be empty.")
            input("\nPress Enter to continue...")
            return
        
        try:
            print("\nChoose encoding format:")
            print("  1. Base-4 (Quaternary)")
            print("  2. Hexadecimal (Recommended)")
            
            choice = input("\nSelect format [1/2]: ").strip()
            
            if choice == '1':
                encoded = self.encoder.encode(text)
                format_name = "Base-4"
            else:
                encoded = self.encoder.encode_to_hex(text)
                format_name = "Hexadecimal"
            
            print(f"\nSUCCESS: Encoded successfully ({format_name}):")
            print("+" + "-" * 58 + "+")
            print(f"| {encoded[:56]}")
            if len(encoded) > 56:
                for i in range(56, len(encoded), 56):
                    print(f"| {encoded[i:i+56]}")
            print("+" + "-" * 58 + "+")
            
            # Option to save to file
            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Enter filename: ").strip()
                if not filename:
                    filename = "encoded_output.txt"
                
                try:
                    with open(filename, 'w') as f:
                        f.write(encoded)
                    print(f"SUCCESS: Saved to '{filename}'")
                except IOError as e:
                    print(f"ERROR: Failed to save file - {e}")
        
        except Exception as e:
            print(f"ERROR: Encoding failed - {e}")
        
        input("\nPress Enter to continue...")
    
    def decode_text(self):
        """
        Handle text decoding operation.
        Prompts for encoded text and format, displays decoded result.
        """
        print("\n" + "-" * 60)
        print("DECODE TEXT")
        print("-" * 60)
        
        encoded = input("\nEnter encoded text (or 'back' to return): ").strip()
        if encoded.lower() == 'back':
            return
        
        if not encoded:
            print("ERROR: Encoded text cannot be empty.")
            input("\nPress Enter to continue...")
            return
        
        try:
            print("\nChoose encoding format:")
            print("  1. Base-4 (Quaternary)")
            print("  2. Hexadecimal")
            
            choice = input("\nSelect format [1/2]: ").strip()
            
            if choice == '1':
                if not all(c in '0123' for c in encoded):
                    raise ValueError("Invalid Base-4 format. Only digits 0-3 allowed.")
                decoded = self.encoder.decode(encoded)
            else:
                if not all(c in '0123456789abcdefABCDEF' for c in encoded):
                    raise ValueError("Invalid hexadecimal format.")
                decoded = self.encoder.decode_from_hex(encoded)
            
            print(f"\nSUCCESS: Decoded successfully:")
            print("+" + "-" * 58 + "+")
            
            # Handle long decoded text
            if len(decoded) > 200:
                print(f"| {decoded[:200]}...")
                print(f"| (truncated, total length: {len(decoded)} characters)")
            else:
                for i in range(0, len(decoded), 56):
                    print(f"| {decoded[i:i+56]}")
            
            print("+" + "-" * 58 + "+")
            
            # Option to save to file
            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Enter filename: ").strip()
                if not filename:
                    filename = "decoded_output.txt"
                
                try:
                    with open(filename, 'w') as f:
                        f.write(decoded)
                    print(f"SUCCESS: Saved to '{filename}'")
                except IOError as e:
                    print(f"ERROR: Failed to save file - {e}")
        
        except ValueError as e:
            print(f"ERROR: {e}")
        except Exception as e:
            print(f"ERROR: Decoding failed - {e}")
            print("NOTE: Verify correct key and format selection.")
        
        input("\nPress Enter to continue...")
    
    def encode_file(self):
        """
        Handle file encoding operation.
        Reads file content, encodes it, and saves to new file.
        """
        print("\n" + "-" * 60)
        print("ENCODE FILE")
        print("-" * 60)
        
        filepath = input("\nEnter file path (or 'back' to return): ").strip()
        if filepath.lower() == 'back':
            return
        
        # Remove quotes if present
        filepath = filepath.strip('"\'')
        
        if not os.path.exists(filepath):
            print(f"ERROR: File not found - {filepath}")
            input("\nPress Enter to continue...")
            return
        
        try:
            # Read file content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content:
                print("ERROR: File is empty.")
                input("\nPress Enter to continue...")
                return
            
            file_size = len(content)
            print(f"INFO: File size - {file_size} characters")
            
            # Select encoding format
            print("\nChoose encoding format:")
            print("  1. Base-4 (Quaternary)")
            print("  2. Hexadecimal (Recommended)")
            
            choice = input("\nSelect format [1/2]: ").strip()
            
            print("\nProcessing...")
            
            if choice == '1':
                encoded = self.encoder.encode(content)
                format_ext = ".b4"
            else:
                encoded = self.encoder.encode_to_hex(content)
                format_ext = ".hex"
            
            # Generate output filename
            path = Path(filepath)
            output_file = str(path.stem) + "_encoded" + format_ext
            
            # Save encoded content
            with open(output_file, 'w') as f:
                f.write(encoded)
            
            print(f"SUCCESS: File encoded successfully")
            print(f"Input:  {filepath}")
            print(f"Output: {output_file}")
            print(f"Size:   {len(encoded)} characters")
        
        except UnicodeDecodeError:
            print("ERROR: File contains non-UTF-8 data.")
            print("NOTE: This tool is designed for text files only.")
        except IOError as e:
            print(f"ERROR: File operation failed - {e}")
        except Exception as e:
            print(f"ERROR: Encoding failed - {e}")
        
        input("\nPress Enter to continue...")
    
    def decode_file(self):
        """
        Handle file decoding operation.
        Reads encoded file, decodes content, and saves to new file.
        """
        print("\n" + "-" * 60)
        print("DECODE FILE")
        print("-" * 60)
        
        filepath = input("\nEnter file path (or 'back' to return): ").strip()
        if filepath.lower() == 'back':
            return
        
        # Remove quotes if present
        filepath = filepath.strip('"\'')
        
        if not os.path.exists(filepath):
            print(f"ERROR: File not found - {filepath}")
            input("\nPress Enter to continue...")
            return
        
        try:
            # Read encoded file
            with open(filepath, 'r') as f:
                encoded = f.read().strip()
            
            if not encoded:
                print("ERROR: File is empty.")
                input("\nPress Enter to continue...")
                return
            
            # Auto-detect format from extension
            path = Path(filepath)
            ext = path.suffix.lower()
            
            if ext == '.b4':
                choice = '1'
                print("INFO: Detected Base-4 format")
            elif ext == '.hex':
                choice = '2'
                print("INFO: Detected Hexadecimal format")
            else:
                print("\nChoose encoding format:")
                print("  1. Base-4 (Quaternary)")
                print("  2. Hexadecimal")
                choice = input("\nSelect format [1/2]: ").strip()
            
            print("\nProcessing...")
            
            if choice == '1':
                if not all(c in '0123' for c in encoded):
                    raise ValueError("Invalid Base-4 format in file.")
                decoded = self.encoder.decode(encoded)
            else:
                if not all(c in '0123456789abcdefABCDEF' for c in encoded):
                    raise ValueError("Invalid hexadecimal format in file.")
                decoded = self.encoder.decode_from_hex(encoded)
            
            # Generate output filename
            output_file = str(path.stem).replace('_encoded', '') + "_decoded.txt"
            
            # Save decoded content
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decoded)
            
            print(f"SUCCESS: File decoded successfully")
            print(f"Input:  {filepath}")
            print(f"Output: {output_file}")
            print(f"Size:   {len(decoded)} characters")
        
        except ValueError as e:
            print(f"ERROR: {e}")
        except IOError as e:
            print(f"ERROR: File operation failed - {e}")
        except Exception as e:
            print(f"ERROR: Decoding failed - {e}")
            print("NOTE: Verify correct key and format selection.")
        
        input("\nPress Enter to continue...")
    
    def change_key(self):
        """
        Handle key change operation.
        Prompts for confirmation before changing encryption key.
        """
        print("\n" + "-" * 60)
        print("CHANGE KEY")
        print("-" * 60)
        print(f"\nCurrent key: {'*' * len(self.key)}")
        
        confirm = input("\nConfirm key change? (y/n): ").strip().lower()
        if confirm == 'y':
            self.get_key()
        else:
            print("Operation cancelled.")
            input("\nPress Enter to continue...")
    
    def run(self):
        """
        Main application loop.
        Displays menu and handles user selections until exit.
        """
        self.clear_screen()
        self.print_header()
        
        print("Welcome to BinSwap - Simple Key-Based Encoder/Decoder\n")
        print("WARNING: This tool is for personal, low-security use only.")
        print("         Do not use for highly sensitive data.\n")
        
        # Initialize encryption key
        self.get_key()
        
        while True:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            choice = input("Select an option [1-6]: ").strip()
            
            if choice == '1':
                self.encode_text()
            elif choice == '2':
                self.decode_text()
            elif choice == '3':
                self.encode_file()
            elif choice == '4':
                self.decode_file()
            elif choice == '5':
                self.change_key()
            elif choice == '6':
                print("\n" + "=" * 60)
                print("Thank you for using BinSwap.")
                print("=" * 60 + "\n")
                sys.exit(0)
            else:
                print("ERROR: Invalid option. Please select 1-6.")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        app = BinSwapTUI()
        app.run()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        print("Goodbye.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        sys.exit(1)