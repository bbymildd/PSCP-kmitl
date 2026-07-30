"""roman"""
def main():
    """roman"""
    num = int(input())

    if num < 0:
        print("Error : Please input positive number")
    elif not num or num > 9:
        print("Error : Out of range")
    elif num <= 3:
        print("I" * num)
    elif num == 4:
        print("IV")
    elif num <= 8:
        print("V", "I" * (num % 5), sep="")
    else:
        print("IX")
main()
