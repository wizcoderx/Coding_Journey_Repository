//Write a function that counts the number of vowels (`a`, `e`, `i`, `o`, `u`) in a given string.

#include <iostream>
#include <string>

using namespace std;

int countVowels(string str) {
    int count = 0;
    for (char ch : str) {
        char lowerCh = tolower(ch); // Make case-insensitive
        if (lowerCh == 'a' || lowerCh == 'e' || lowerCh == 'i' || lowerCh == 'o' || lowerCh == 'u') {
            count++;
        }
    }
    return count;
}

int main() {
    string str = "Hello, World!";
    int vowelCount = countVowels(str);
    cout << "Number of vowels: " << vowelCount << endl;
    return 0;
}