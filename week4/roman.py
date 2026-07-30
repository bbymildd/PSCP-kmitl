"""roman"""
def main():
    """roman"""
    num = int(input())

    if 0 < num <= 9:
        if num == 1:
            print("I")
        elif num == 2:
            print("II")
        elif num == 3:
            print("III")
        elif num == 4:
            print("IV")
        elif num == 5:
            print("V")
        elif num == 6:
            print("VI")
        elif num == 7:
            print("VII")
        elif num == 8:
            print("VIII")
        elif num == 9:
            print("IX")
        else:
            print("X")
    elif 0 <= num < 1 or num > 9:
        print("Error : Out of range")
    else:
        print("Error : Please input positive number")
main()
