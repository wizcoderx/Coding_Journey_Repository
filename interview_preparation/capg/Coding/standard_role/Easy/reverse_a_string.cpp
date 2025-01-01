//Write a function that takes a string as input and returns the string reversed.

#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    int n = s.length();
    string reversed = "";
    for (int i = 0; i < n/2; i++ ) {
        char temp = s[i];
        s[i] = s[n-i-1];
        s[n-i-1] = temp;
    }
    return s;
}

int main() {
    string s = "You Gang";
    cout << reverseString(s) << endl;
}