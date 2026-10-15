"""run"""
def main():
    """run"""
    day, goal = map(int, input().split())
    run = list(map(int, input().split()))

    total = 0

    for i in range(day):
        total += run[i]

        if total >= goal:
            print(i + 1)
            break
    else:
        print("-1")


main()
