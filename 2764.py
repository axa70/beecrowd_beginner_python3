date_input = input()

day, month, year = map(str, date_input.split("/"))

'''
print(day)
print(month)
print(year)
'''

#format 01
print(f"{month}/{day}/{year}")

#format 02
print(f"{year}/{month}/{day}")

#format 03
print(f"{day}-{month}-{year}")
