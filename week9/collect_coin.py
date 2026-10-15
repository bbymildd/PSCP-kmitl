"""magic"""
def main():
    """coin"""
    arena = int(input())

    fire = 0
    water = 0
    earth = 0

    for _ in range(arena):
        f1, w1, e1, f2, w2, e2 = map(int, input().split())

        fire += max(f1, f2)
        water += max(w1, w2)
        earth += max(e1, e2)

    total = fire + water + earth

    print("Total:", total)
    print("Fire:", fire)
    print("Water:", water)
    print("Earth:", earth)

    if fire > water + earth:
        print("Bonus: YES")
    else:
        print("Bonus: NO")

main()
