"""sellcar"""
def main():
    """sellcar"""
    car = int(input())
    cars = []

    for _ in range(car):
        price, eff = map(int, input().split())
        cars.append((price, eff))

    no_buy = 0

    for i in range(car):
        price, eff = cars[i]
        cannot_buy = False

        for j in range(car):
            if i != j:
                other_price, other_eff = cars[j]

                if other_price < price and other_eff > eff:
                    cannot_buy = True
                    break

        if cannot_buy:
            no_buy += 1

    print(no_buy)

main()
