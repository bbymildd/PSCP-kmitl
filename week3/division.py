"""division"""
def main():
    """division"""
    num1 = int(input())
    num2 = int(input())

    if not num1 % num2:
        print("yes")
    elif num1 % num2 > 0:
        print("no")

main()
