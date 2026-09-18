"""movie"""
def main():
    """movie"""
    all_seat = int(input())

    while all_seat > 0:
        try:
            age, ticket = map(int, input().split())
        except EOFError:
            break

        if age < 15:
            print(-1)
            continue

        if ticket > all_seat:
            print(-2)
            continue

        if age >= 60:
            price = 75
        elif age <= 22:
            price = 120
        else:
            price = 150

        total = price * ticket
        all_seat -= ticket

        print(total, all_seat)

main()
