//Create a program that takes a string input and checks whether it is a palindrome.

#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string str) {
    if (str.length() <=1) {
        return true;
    }
    else {
        if (str[0] == str[str.length() - 1]) {
            return isPalindrome(str.substr(1, str.length() - 2));
        }
        else {
            return false;
        }
    }
}

int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;
    if (isPalindrome(str)) {
        cout << str << " is a palindrome";
    }
    else {
        cout << str << " is not a palindrome";
    }
}