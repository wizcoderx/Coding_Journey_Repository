#include <iostream>
using namespace std;

void printFibonacci(int num1, int num2) {
    int n1 = num1, n2 = num2, n3;
    cout << n1 << " " << n2 << " ";
    for (int i = 2; i < 10; ++i) {
        n3 = n1 + n2;
        cout << n3 << " ";
        n1 = n2;
        n2 = n3;
    }
    cout << endl;
}

int main() {
    int num1, num2;
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;
    printFibonacci(num1, num2);
    return 0;
}