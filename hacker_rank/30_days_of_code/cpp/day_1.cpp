/*
Task:
1. Declare 3 variables: one of type int, one of type double, and one of type String.
2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
3. Use the '+' operator to perform the following operations:
    1. Print the sum of 'i' plus your int variable on a new line.
    2. Print the sum of 'd' plus your double variable to a scale of one decimal place on a new line.
    3. Concatenate 's' with the string you read as input and print the result on a new line.
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>
#include<limits>
#include <iomanip>

using namespace std;


int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    int i2;
    double d2;
    string s2;

    cin>>i2>>d2;
    getline(cin>> ws, s2);

    cout<<(i + i2)<<endl; //int output
    cout<< fixed << setprecision(1) << (d + d2)<<endl;
    cout<<(s + s2)<<endl; //string output

    return 0;
}
