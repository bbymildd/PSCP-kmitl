"""highest"""
def main():
    """highest"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    high = num1
    if num2 > high:
        high = num2
    if num3 > high:
        high = num3

    print(high)

main()
