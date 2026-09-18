"""balance"""
def main():
    """balance"""
    work = int(input())
    sadday = 0
    wowday = 0

    for _ in range(work):
        time = int(input())
        if time > 18:
            sadday += 1
        else:
            wowday += 1

    extra_day = sadday - wowday - 1

    if extra_day < 0:
        extra_day = 0

    print(work + extra_day)

main()
