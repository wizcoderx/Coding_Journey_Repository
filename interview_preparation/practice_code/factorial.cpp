//Write a C++ program to find the factorial of a given number using recursion.

#include <iostream>
using namespace std;

int factorial(int n) {
   if (n==0) {
        return 1;
   }

   else {
    return n* factorial(n-1);
   }
}

int main(){
    int n;
    cout << "Enter a number";
    cin >> n;
    cout << "Factorial of " << n << " is " << factorial(n);
}