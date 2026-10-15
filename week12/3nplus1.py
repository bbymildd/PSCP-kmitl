"""three"""
while True:
    num = int(input())

    if not num:
        break

    count = 1

    while num != 1:
        if not num % 2:
            num = num // 2
        else:
            num = num * 3 + 1

        count += 1

    print(count)
