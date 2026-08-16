"""rome"""
def main():
    """rome"""
    num = input()
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    e = int(num[4])

    if a > 5:
        first = 9
    elif b > 5:
        first = 10
    elif c > 5:
        first = 11
    elif d > 5:
        first = 12
    elif e > 5:
        first = 14
    else:
        first = 13

    if num == num[::-1]:
        if a + e > 5:
            second = 1
        elif b * d > 5:
            second = 2
        else:
            second = 0
    else:
        if e and a // e > 5:
            second = 1
        elif b - e > 5:
            second = 2
        else:
            second = 0

    total = a + b + c + d + e
    multiply = a * b * c * d * e

    if total > 25:
        third = 1
    elif multiply > 55:
        third = 2
    else:
        third = 0

    print(first, second, third, sep="")


main()
