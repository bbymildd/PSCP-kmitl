"""game"""
def main():
    """game"""
    base = int(input())
    bonus =int(input())
    day = int(input())

    if day > 3:
        total = (base + bonus) * 1.5
    else:
        total = base + bonus

    if total >= 1500:
        rank = 5
    elif total >= 1000:
        rank = 4
    elif total >= 500:
        rank = 3
    elif total >= 200:
        rank = 2
    else:
        rank = 1

    if rank == 5 and day >= 7:
        key = 99
    elif rank == 4 and bonus > 300:
        key = 88
    else:
        key = 0

    print(int(total))
    print(rank)
    print(key)

main()
