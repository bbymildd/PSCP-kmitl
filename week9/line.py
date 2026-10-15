"""line"""
def main():
    """line"""
    _, _ = map(int, input().split())

    all_tall = list(map(int, input().split()))
    all_position = list(map(int, input().split()))

    for who in all_position:
        position = who - 1

        if not position:
            print(0)
            continue

        whotall = max(all_tall[:position])

        if all_tall[position] > whotall:
            chair = 0
        else:
            chair = whotall - all_tall[position] + 1

        print(chair)

main()
