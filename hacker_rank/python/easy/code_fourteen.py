'''
The python code has solved the hacker rank questioned mentioned in the URL:  https://www.hackerrank.com/challenges/python-lists
'''

if __name__ == '__main__':
    alis = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alis.append([name,score])

second_highest = sorted(set([score for name, score in alis]))[1]
print("\n".join(sorted([name for name, score in alis if score == second_highest])))
