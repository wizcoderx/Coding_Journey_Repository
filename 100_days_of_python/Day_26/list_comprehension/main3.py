with open("file1.txt", "r") as file1:
    content1 = file1.read().splitlines()


with open("file2.txt", "r") as file2:
    content2 = file1.read().splitlines()


number1 = [int(num_str) for num_str in content1]
number2 = [int(num_str) for num_str in content2]

result = [num for num in number1 if num in number2]

print(result)