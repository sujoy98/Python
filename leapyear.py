year = int(input("enter year : "))
if (year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0):
    print('Leap')
else:
    print('notLeap')

''' using function :-

def is_leap(year):
    return((year % 4 ==0) and (year % 100 != 0)) or (year % 400 == 0)
year = int(input())
print(is_leap(year)) '''
