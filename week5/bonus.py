"""bonus"""
def main():
    """bonus"""
    _type, age, money = input().split()
    age = int(age)
    money = int(money)

    if _type == "M":
        if 0 < age <= 5:
            print(int(0.06 * money) + 1500)
        elif age <= 10:
            print(int(0.08 * money) + 1500)
        elif age > 10:
            print(int(0.10 * money) + 1500)

    elif _type == "B":
        if 0 < age <= 5:
            print(int(0.05 * money) + 1000)
        elif age <= 10:
            print(int(0.06 * money) + 1000)
        elif age > 10:
            print(int(0.07 * money) + 1000)

    else:
        if 0 < age <= 5:
            print(int(0.04 * money) + 500)
        elif age <= 10:
            print(int(0.05 * money) + 500)
        elif age > 10:
            print(int(0.06 * money) + 500)

main()
