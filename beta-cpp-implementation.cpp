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

int main(){
    std::string myString = "SUPERSECRETPASSWORD";
    std::cout << strToBinary(myString);
}
