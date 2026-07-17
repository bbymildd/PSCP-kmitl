"""lowest"""
def main():
    """lowest"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    lowest = num1
    if num2 < lowest:
        lowest = num2
    if num3 < lowest:
        lowest = num3

    print(lowest)

main()
