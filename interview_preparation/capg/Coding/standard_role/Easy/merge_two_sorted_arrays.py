#Write a function to merge two sorted arrays into a single sorted array.

def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6])) #[1, 2, 3, 4, 5, 6]