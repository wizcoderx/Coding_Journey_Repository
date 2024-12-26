//Write a program that uses a switch-case to perform basic arithmetic operations (addition, subtraction, multiplication, division) based on user input.

#include <iostream>
using namespace std;

int main() {
    char op;
    int num1, num2;
    cout << "Enter an operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    switch(op) {
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2;
            break;
        case '-':
        cout << num1 << " - " << num2 << " = " << num1 - num2;
            break;
        case '*':
        cout << num1 << " * " << num2 << " = " << num1 * num2;
            break;
        case '/':
        cout << num1 << " / " << num2 << " = " << num1 / num2;
            break;
        default:
            cout << "Invalid operator";
    }
}