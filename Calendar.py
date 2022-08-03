import calendar

year = int(input("enter year in numbers: "))
month = int(input('enter month in numbers: '))

c = calendar.month(year, month)
print (c)