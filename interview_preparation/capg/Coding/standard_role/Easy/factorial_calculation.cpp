//Write a function that calculates the factorial of a non-negative integer.

#include <iostream>
using namespace std;

int factorial(double n) {
    if (n==0) {
        return 1;
    }
    else {
        return n*factorial(n-1);
    }
}

int main() {
    cout<<factorial(5)<<endl;
}