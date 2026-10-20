"""calendar"""
def main():
    """calendar"""
    day = int(input())
    month = int(input())
    year = int(input())

    current = year * 360 + month * 30 + day
    deadline = 2569 * 360 + 10 * 30 + 2

    remain = deadline - current

    if remain < 0:
        remain = 0

    print(remain)

main()
