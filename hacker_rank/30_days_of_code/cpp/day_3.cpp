//https://www.hackerrank.com/challenges/30-conditional-statements

#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <limits>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

int main()
{
    string N_temp;
    getline(cin, N_temp);

    int N = stoi(ltrim(rtrim(N_temp)));

    if (N % 2 != 0) {
        cout << "Weird";
    } else {
        if (N >= 2 && N <= 5) {
            cout << "Not Weird";
        } else if (N >= 6 && N <= 20) {
            cout << "Weird";
        } else if (N > 20) {
            cout << "Not Weird";
        }
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), [](unsigned char c) { return !isspace(c); })
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), [](unsigned char c) { return !isspace(c); }).base(),
        s.end()
    );

    return s;
}
