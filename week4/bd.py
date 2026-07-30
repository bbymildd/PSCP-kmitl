"""bd"""
from datetime import date
def main():
    """bd"""
    year1 = int(input())
    mon1 = int(input())
    day1 = int(input())
    year2 = int(input())
    mon2 = int(input())
    day2 = int(input())

    date1 = date(year1, mon1, day1)
    date2 = date(year2, mon2, day2)

    diff = abs((date1 - date2).days)

    if diff <= 7:
        print("0")
    elif date1 > date2:
        print("2")
    else:
        print("1")

main()
