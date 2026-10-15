"""bridge"""
def main():
    """bridge"""
    long , many = map(int, input().split())
    bridges = []

    for _ in range(many):
        startt, endd = map(int, input().split())
        bridges.append((startt,endd))

    mak = 0
    for pos in range(long):
        count = 0

        for startt, endd in bridges:
            if startt < pos + 0.5 < endd:
                count += 1

        if count > mak:
            mak = count

    print(mak)

main()
