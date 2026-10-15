"""cave"""
def main():
    """cave"""
    long = int(input())
    cave = list(map(int,input().split()))
    walk = input()

    position = cave.index(1)

    for direct in walk:
        if direct == "R":
            new = position + 1
        else:
            new = position - 1

        if 0 <= new < long:

            if cave[new] == 2:
                cave[position] = 0
                position = new
                cave[position] = 1
                break
            cave[position] = 0
            position = new
            cave[position] = 1
    print(*cave)

main()
