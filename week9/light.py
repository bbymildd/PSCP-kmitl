"""light"""
def main():
    """light"""
    num = int(input())
    light = [False] * 360

    for _ in range(num):
        start, end = map(int, input().split())

        if start < end:
            for angle in range(start, end):
                light[angle] = True
        else:
            for angle in range(start, 360):
                light[angle] = True
            for angle in range(end):
                light[angle] = True

    if all(light):
        print(360)
        return

    long = 0
    count = 0

    for angle in range(720):
        if light[angle % 360]:
            count += 1
            long = max(long, count)
        else:
            count = 0

    print(min(long, 360))

main()
