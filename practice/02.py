"""num"""
def main():
    """num"""
    num = input()

    if num.count("0") == len(num):
        print("0")
        return

    result = 1
    for number in num:
        if number != "0":
            result *= int(number)
    print(result)

main()
