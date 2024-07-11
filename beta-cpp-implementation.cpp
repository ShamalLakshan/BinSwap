#include <string>
#include <bits/stdc++.h>
#include <iostream>


std::string strToBinary(std::string s){
    int n = s.length();
    std::string output = "";

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

        output += bin + " ";
    }
    return output;
}


std::string reverseString(std::string input_string){
    reverse(input_string.begin(), input_string.end());

    return input_string;
}


std::string keyExpansion(std::string original_key, int original_input_length){
    std::string binary_key = strToBinary(original_key);



    return binary_key;
}


std::string simpleXor(std::string user_input, std::string key){
    std::string ans = "";
    int n = user_input.length();

    // Loop to iterate over the
    // Binary Strings
    for (int i = 0; i < n; i++)
    {
        // If the Character matches
        if (user_input[i] == key[i])
            ans += "0";
        else
            ans += "1";
    }
    return ans;
}


int main(){
    std::string myString;
    std::string myKey;

    std::cout << "Enter a String to Encode: \n";
    std::getline(std::cin >> std::ws,  myString);

    int user_input_length = myString.length();

    std::cout << "#########################################################################" << std::endl;
    
    std::cout << "Original String: " << myString << std::endl;

    std::string binary_string = strToBinary(myString);
    std::cout << "Binary String: " << binary_string << std::endl;
    
    std::string reversed_binary_string = reverseString(binary_string);
    std::cout << "Reversed Binary String: " << reversed_binary_string << std::endl;

    std::cout << "#########################################################################" << std::endl;

    std::cout << "Enter a Key to Encode: ";
    std::getline(std::cin >> std::ws,  myKey);

    std::cout << "#########################################################################" << std::endl;

    // std::string expanded_key = keyExpansion(myKey, user_input_length);
    // std::cout << "Expanded Key (Bin): " << expanded_key << std::endl;

    std::string binary_key = strToBinary(myKey);
    std::cout << "Binary key: " << binary_key << std::endl;


    std::string xored = simpleXor(binary_string, binary_key);
    std::cout << "Xored String: " << xored << std::endl;

    
    std::string back_xored = simpleXor(binary_key, xored);
    std::cout << "Back Xor key and out: " << back_xored << std::endl;

    std::cout << "#########################################################################" << std::endl;

    int multiplier = (binary_string.length() / binary_key.length());
    std::cout << "Multiplier: " << multiplier << std::endl; 

}
