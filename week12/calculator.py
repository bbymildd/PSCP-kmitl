"""cal"""
def main():
    """cal"""
    num = int(input())

    if num == 1:
        print(1)
        return

    count = num

    start = 1
    digits = 1

    while start <= num:
        end = min(num, start * 10 - 1)
        count += (end - start + 1) * (digits - 1)
        start *= 10
        digits += 1

    count += num

    print(count)

main()
