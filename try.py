"""triangle"""
def main():
    """triangle"""
    row = int(input())

    for i in range(1, row + 1):
        space = " " * (i - 1)
        number = f"{i:02} " * (row - i + 1)
        print(space + number.rstrip())

main()
