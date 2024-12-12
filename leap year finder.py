
year = int(input("what year would you like to know is a leap year? " ))

if (year % 100 == 0 and year % 400 == 0): #this checks if 100 and 400 is divisable by using "%" for mod, which is used for returning the remainder of a division operation.
    print("this yeyar {} is a leap year".format(year))
elif(year % 4 == 0 and year % 100 != 0): #this checks if the year is ddevisaable by 4, but not NOT by 100. this identifies most leap years, like 2024.
    print("this year is {} is a leap year".format(year))
else:
    print("this year {} is not a leap year".format(year))
