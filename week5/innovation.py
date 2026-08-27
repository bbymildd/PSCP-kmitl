"""innovation"""
def main():
    """innovation"""
    school = input().upper()

    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    first = ord(school[0])
    last = ord(school[-1])

    level1 = []

    for i in range(10):
        if (i + 1) % 2 == 1:
            value = first + num[i]
        else:
            value = last - num[i]

        level1.append(value)

    level2 = []

    for value in level1:
        value %= len(school)
        value %= 10
        level2.append(value)

    password = level2[2:8]

    print(*password)

main()
