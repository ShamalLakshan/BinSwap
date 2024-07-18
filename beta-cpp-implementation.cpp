#include <string>
#include <bits/stdc++.h>
#include <iostream>


std::vector<std::string> strToBinary(std::string s){
    int n = s.length();
    std::vector<std::string> output;

    for (int i = 0; i <= n; i++){
        // convert each char to
        // ASCII value
        int val = int(s[i]);

        // Convert ASCII value to binary
        std::string bin = "";
        while (val > 0){
            (val % 2)? bin.push_back('1') :
                    bin.push_back('0');
            val /= 2;
        }
        reverse(bin.begin(), bin.end());

        output.push_back(bin);
    }
    return output;
}


std::vector<std::string> reverseString(std::vector<std::string> input_string){
    reverse(input_string.begin(), input_string.end());

    return input_string;
}


std::vector<std::string> keyExpansion(std::vector<std::string> original_key, std::vector<std::string> original_input){
    int difference = (original_input.size() - 1) - (original_key.size() - 1);

    std::cout << difference << std::endl;
    std::vector<std::string> expanded_key = original_key;


    for(int i = 0; i < difference; i++){
        expanded_key.push_back("00000000");
    }

    return expanded_key;
}


std::vector<std::string> simpleXor(std::vector <std::string> user_input, std::vector<std::string> key){
    std::vector<std::string> xored_string;
    int n = user_input.size();

    for(int i = 0; i < n; i++){
        std::string octet = "";
        std::string single_octet_input = user_input[i];
        std::string single_octet_key = key[i];
        for(char bit : single_octet_input){
            if (bit == single_octet_key[i])
                octet += "0";
            else
                octet += "1";
        }
        xored_string.push_back(octet);
    }
    return xored_string;
}

std::string encodeString(const std::string& input, const std::string& key) {
    std::vector<std::string> binary_string = strToBinary(input);
    std::cout << "Original binary: ";
    printBinary(binary_string);

    std::vector<std::string> reversed_binary_string = reverseString(binary_string);
    std::cout << "Reversed binary: ";
    printBinary(reversed_binary_string);

}


int main(){
    std::string myString;
    std::string myKey;

    std::cout << "Enter a String to Encode: \n";
    std::getline(std::cin >> std::ws,  myString);

    int user_input_length = myString.length();

    std::cout << "#########################################################################" << std::endl;
    
    std::cout << "Original String: " << myString << std::endl;
    std::cout << "Original Binary String: " << myString << std::endl;

    std::vector<std::string> binary_string = strToBinary(myString);
    for(std::string octet : binary_string){
        std::cout << octet << " ";
    }
    std::cout << std::endl;

    std::cout << std::endl;

    std::cout << "Reversed Binary String: " << myString << std::endl;
    std::vector<std::string> reversed_binary_string = reverseString(binary_string);
    for(std::string octet : reversed_binary_string){
        std::cout << octet << " ";
    }
    std::cout << std::endl;

    std::cout << "#########################################################################" << std::endl;
    std::cout << "Enter a Key to Encode: ";
    std::getline(std::cin >> std::ws,  myKey);
    std::cout << "Original Key: " << myKey << std::endl;

    std::cout << "Binary key" << std::endl;
    std::vector<std::string> binary_key = strToBinary(myKey);
    for(std::string octet : binary_key){
        std::cout << octet << " ";
    }
    std::cout << std::endl;

    std::cout << "#########################################################################" << std::endl;
    std::cout << "Expanded key" << std::endl;
    std::vector<std::string> expanded_key = keyExpansion(binary_key, reversed_binary_string);
    for(std::string octet : expanded_key){
        std::cout << octet << " ";
    }
    std::cout << std::endl;


    std::cout << "#########################################################################" << std::endl;
    std::cout << "XORing" << std::endl;

    std::vector<std::string> xored = simpleXor(reversed_binary_string, expanded_key);
    for(std::string octet : xored){
        std::cout << octet << " ";
    }
    std::cout << std::endl;

    std::cout << "#########################################################################" << std::endl;
    std::cout << "verifying XOR" << std::endl;

    std::vector<std::string> reverse_xored = simpleXor(xored, expanded_key);
    for(std::string octet : reverse_xored){
        std::cout << octet << " ";
    }
    std::cout << std::endl;

    // std::string back_xored = simpleXor(binary_key, xored);
    // std::cout << "Back Xor key and out: " << back_xored << std::endl;

    // std::cout << "#########################################################################" << std::endl;

    // int multiplier = (binary_string.length() / binary_key.length());
    // std::cout << "Multiplier: " << multiplier << std::endl; 

}
