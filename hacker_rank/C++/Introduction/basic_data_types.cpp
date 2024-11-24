/*
Input Format
Input consists of the following space-separated values: int, long, char, float,
and double, respectively.

Output Format
Print each element on a new line in the same order it was received as input.
Note that floating point value should be correct up to 3 decimal places and
the double to 9 decimal places.

Sample Input
3 12345678912345 a 334.23 14049.30493

Sample Output
3
12345678912345
a
334.230
14049.304930000
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;



int main() {
    int a;
    long b;
    char c;
    float d;
    double e;

    cin>>a>>b>>c>>d>>e;

        // Correcting the output statements by using << instead of format specifiers
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << fixed << setprecision(6) << d << endl; // float with 6 decimal places
    cout << fixed << setprecision(6) << e << endl; // double with 6 decimal places

    return 0;
}
