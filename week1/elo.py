"""elo"""
def main():
    """elo"""
    ra = int(input())
    rb = int(input())
    font = input()
    rea = rb - ra
    reb = ra - rb
    ea = 1 / (1 + (10 ** (rea/400)))
    eb = 1 / (1 + (10 ** (reb/400)))

    if font == "A":
        print(f"{ea:.2f}")
    elif font == "B":
        print(f"{eb:.2f}")

main()
