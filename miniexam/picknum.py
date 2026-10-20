"""picknum"""
def main():
    """picknum"""
    num = list(map(int, input().split()))
    po = 0
    ne = 0
    zero = 0
    for number in num:
        if number > 0:
            po += 1
        elif number < 0:
            ne += 1
        else:
            zero += 1
    print(f"Positive: {po}")
    print(f"Negative: {ne}")
    print(f"Zero: {zero}")

main()
