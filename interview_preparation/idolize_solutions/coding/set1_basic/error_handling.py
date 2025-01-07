#Explain the purpose of `try-except` blocks in Python. Provide an example where they are used.
'''
# try-except block in Python
try:
    # code that may raise an exception
    pass
except Exception as e:
    # code that will run if an exception is raised
    pass

'''

# Example
# In this example, we are trying to open a file that does not exist. If the file does not exist, an exception will be raised, and we will handle it using a try-except block.
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError as e:
    print("File not found:", e)