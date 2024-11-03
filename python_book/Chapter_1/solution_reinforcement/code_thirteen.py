'''
Write a short Python function that counts the number of vowels in a given character string.
'''


def count_vowels(string):
    count = 0
    vowels_list = ['a','e','i','o','u']
    for i in string.lower():
        if i in vowels_list:
            count+=1

    return count

# Example usage
input_string = "lecture"
vowel_count = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {vowel_count}")