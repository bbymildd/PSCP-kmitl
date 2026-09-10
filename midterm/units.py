"""Units"""
def main():
    """Units"""
    num = float(input())
    unit1 = input()
    unit2 = input()

    if unit1 == unit2:
        print(f"{num:.4f}")
    else:
        if unit1 == "NIU":
            num *= 1920
        elif unit1 == "KUEP":
            num *= 160
        elif unit1 == "SOK":
            num *= 80
        elif unit1 == "WA":
            num *= 20

        if unit2 == "NIU":
            print(f"{num / 1920:.4f}")
        elif unit2 == "KUEP":
            print(f"{num / 160:.4f}")
        elif unit2 == "SOK":
            print(f"{num / 80:.4f}")
        elif unit2 == "WA":
            print(f"{num / 20:.4f}")
        else:
            print(f"{num:.4f}")

main()
