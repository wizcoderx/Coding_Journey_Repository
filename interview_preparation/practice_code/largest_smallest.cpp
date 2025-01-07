//Implement a program to find the largest and smallest numbers in an array.

#include <iostream>
using namespace std;

int main() {
    int arr[10], n, i, max, min;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    max = arr[0];
    min = arr[0];

    for (int i =1; i <n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
        else if (arr[i] < min) {
            min = arr[i];
        }

    }

    cout<< max<<min;
}