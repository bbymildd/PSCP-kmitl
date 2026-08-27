"""walking"""
def main():
    """walking"""
    walk = input().upper()
    x = 0
    y = 0
    y += walk.count("N")
    y -= walk.count("S")
    x += walk.count("E")
    x -= walk.count("W")

    d = abs(x) + abs(y)

    print(f"{x} {y} {d}")

main()
