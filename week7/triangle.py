"""triangle"""
def main():
    """triangle"""
    num = int(input())

    for line in range(num):
        for col in range(line + 1):
            if not col:
                print("0", end="")
            elif line == num - 1:
                print("0", end="")
            elif col == line:
                print("0", end="")
            else:
                print("1", end="")
        print()

main()
