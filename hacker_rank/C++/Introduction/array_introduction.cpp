//https://www.hackerrank.com/challenges/arrays-introduction

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    //take the size for array
    int n;
    cin>>n;
    vector<int> arr(n);
    //take input of numbers inside the array

    for (int i=0;i<n;i++) {
        //take the intput of arry
        cin>>arr[i];
    }

    for ( int i=n-1; i>=0; i--) {
        cout<<arr[i]<<" ";
    }

    return 0;
}
