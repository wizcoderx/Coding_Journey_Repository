'''
FUNCTION reverse_list(arr):
    start = 0
    end = len(arr) - 1

    WHILE start < end:
        # Swap elements at start and end
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        # Move start and end pointers
        start = start + 1
        end = end - 1

    RETURN arr

'''

def reverse_list(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end
        arr[start], arr[end] = arr[end], arr[start]

        # Move start and end pointers
        start += 1
        end -= 1

    return arr

# Example usage:
data = [1, 2, 3, 4, 5]
reversed_data = reverse_list(data)
print("Reversed list:", reversed_data)
