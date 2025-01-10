#Write a Python function to merge two sorted lists into a single sorted list.

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# test the function
print(merge_sorted_lists([1,2,3,4],[3,4,5]))