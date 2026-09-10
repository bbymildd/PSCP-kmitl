"""thai"""
def main():
    """thai"""
    name = input()
    age = float(input())
    income = float(input())
    card = input()
    mem = float(input())

    if age < 18:
        print(f"{name} NOT ELIGIBLE")
        return

    if age >= 18:
        if card == "Y":
            rank = "GOLD"
            if mem >= 3:
                money = 3500
            else:
                money = 3000
            print(f"{name} {rank} {money}")
        elif income <= 15000:
            rank = "GOLD"
            if mem >= 3:
                money = 3500
            else:
                money = 3000
            print(f"{name} {rank} {money}")
        elif income <= 30000:
            rank = "SILVER"
            if mem >= 3:
                money = 2000
            else:
                money = 1500
            print(f"{name} {rank} {money}")
        else:
            print(f"{name} NOT ELIGIBLE")
main()
