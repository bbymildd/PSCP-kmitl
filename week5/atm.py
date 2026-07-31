"""atm"""
def main():
    """atm"""
    draw = int(input())

    if draw % 100:
        print("ERROR")
        return
    thou = draw // 1000
    draw = draw % 1000
    five = draw // 500
    draw = draw % 500
    hun = draw // 100
    draw = draw % 100

    if thou:
        print(f"1000 = {thou}")
    if five:
        print(f"500 = {five}")
    if hun:
        print(f"100 = {hun}")

main()
