#Write a Python function to read a text file and count the number of lines in it.

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(len(file.readlines()))
    except FileNotFoundError as e:
        print("File not found:", e)
        return -1

file_path = "D:\\Anamay\\Projects\\2024\\Python_Learning\\interview_preparation\\idolize_solutions\\coding\\set1_basic\\file_one.txt"
count_lines(file_path)