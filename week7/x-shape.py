"""xshape"""
def main():
    """xshape"""
    line, sym = input().split()
    line = int(line)

    center = line // 2

    for i in range(line):
        for j in range(line):
            if i == j or i + j == line - 1:
                if sym == "#":
                    print("#", end="")
                else:
                    distance = abs(center - i)
                    print(chr(ord(sym) + distance), end="")
            else:
                print("-", end="")
        print()

main()
