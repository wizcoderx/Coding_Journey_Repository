'''
The python code has solved the hacker rank questioned mentioned in the URL: https://www.hackerrank.com/challenges/calendar-module/
'''
import calendar
month, day, year = list(map(int,input().split()))
ans = calendar.weekday(year, month, day)
print((calendar.day_name[ans]).upper())