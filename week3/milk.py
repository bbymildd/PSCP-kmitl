"""milk"""
def main():
    """milk"""
    price_per = int(input())
    cap = int(input())
    milk = int(input())
    money = int(input())

    if not cap:
        full = money // price_per
        print(full)
        return
    if not money:
        print("0")
    else:
        total_milk = money // price_per
        caps = total_milk
        while caps >= cap:
            exchange = (caps // cap) * milk
            total_milk += exchange
            caps = (caps % cap) + exchange

        print(total_milk)
main()
