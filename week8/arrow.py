"""arrow"""
def main():
    """arrow"""
    direct = input()
    size = int(input())

    for index,arrow in enumerate(direct):
        if arrow == "R":
            for i in range(size):
                print(" " * (i * 2) + "*" * (size - i))

            for i in range(size - 2, -1, -1):
                print(" " * (i * 2) + "*" * (size - i))

        else:
            for i in range(size):
                print(" " * (size - 1 - i) + "*" * (size - i))

            for i in range(size - 2, -1, -1):
                print(" " * (size - 1 - i) + "*" * (size - i))

        if index != len(direct) - 1:
            print()

main()
