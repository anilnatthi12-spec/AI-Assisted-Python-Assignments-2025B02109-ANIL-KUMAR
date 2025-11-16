def is_leap_year(year):
    """Return True if the given year is a leap year, otherwise False."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# --- Call the function ---
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
