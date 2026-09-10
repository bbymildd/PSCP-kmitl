"""thaiplus"""
def main():
    """thaiplus"""
    wallet = int(input())
    day = int(input())

    list_success = 0
    goverspend_total = 0
    monthly = 1000

    for _ in range(day):
        daily = 200
        item = int(input())

        for _ in range(item):
            price = int(input())

            people = price * 40 // 100
            state = price - people

            if state > daily:
                state = daily

            if state > monthly:
                state = monthly

            pay = price - state

            if wallet >= pay:
                wallet -= pay
                daily -= state
                monthly -= state

                list_success += 1
                goverspend_total += state

    print(list_success)
    print(wallet)
    print(goverspend_total)

main()
