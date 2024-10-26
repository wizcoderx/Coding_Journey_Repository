'''

A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. Given an integer, , rotate the array that many steps left and return the result.

Example


After  rotations, .

Function Description

Complete the rotateLeft function in the editor below.

rotateLeft has the following parameters:

int d: the amount to rotate by
int arr[n]: the array to rotate
Returns

int[n]: the rotated array

'''

def rotateLeft(d, arr):
    n = len(arr)
    d = d % n  # In case d is larger than n
    return arr[d:] + arr[:d]  # Rotate left by d positions

# Input handling
n, k = map(int, input().split())  # Input for n and k
arr = list(map(int, input().split()))  # Input the array

# Perform the rotation
rotated_arr = rotateLeft(k, arr)

# Output the result
print(' '.join(map(str, rotated_arr)))
