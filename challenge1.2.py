year = 2005

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
