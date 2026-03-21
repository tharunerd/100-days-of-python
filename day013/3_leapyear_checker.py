
# leapyear checker
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def check_leap_year(year):
    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
year = int(input("Enter a year: "))
check_leap_year(year)
