// Write a C++ program to sort an array of integers in ascending order using the bubble sort algorithm.

#include <iostream>
using namespace std;

int main() {
    int arr[5] = {5, 2, 8, 1, 3};
    int n = 5;
    int temp;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}