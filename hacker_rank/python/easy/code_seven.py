'''
The python code has solved the hacker rank questioned mentioned in the URL: https://www.hackerrank.com/challenges/find-a-string/
'''

def count_substring(string, sub_string):
    total = 0
    for i in range(0, len(string)):
        if string[i:len(string)].startswith(sub_string):
            total +=1
    return total
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)