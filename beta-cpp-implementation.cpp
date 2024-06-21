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


int main(){
    std::string myString;
    std::string myKey;

    std::cout << "Enter a String to Encode: \n";
    std::getline(std::cin >> std::ws,  myString);

    int user_input_length = myString.length();
    
    std::cout << "Original String: " << myString << std::endl;

    std::string binary_string = strToBinary(myString);
    std::cout << "Binary String: " << binary_string << std::endl;
    
    std::string reversed_binary_string = reverseString(binary_string);
    std::cout << "Reversed Binary String: " << reversed_binary_string << std::endl;

    std::cout << "Enter a Key to Encode: \n";
    std::getline(std::cin >> std::ws,  myKey);

    std::string expanded_key = keyExpansion(myKey, user_input_length);
    std::cout << "Expanded Key (Bin): " << expanded_key << std::endl;

}
