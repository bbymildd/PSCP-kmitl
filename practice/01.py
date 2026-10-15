"""kind"""
def main():
    """kind"""
    data = input()
    up = 0
    lo = 0
    num = 0

    for font in data:
        if font.isupper():
            up += 1
        elif font.islower():
            lo += 1
        elif font.isnumeric():
            num += 1
    print(f"{up} {lo} {num}")

main()
