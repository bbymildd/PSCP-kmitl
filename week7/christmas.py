"""light"""
def main():
    """light"""
    color, amount = input().split()
    amount = int(amount)
    see = ["Blue", "Red", "Green"]
    start = {"B": 0, "R": 1, "G": 2}
    result = []

    for i in range(amount):
        result.append(see[(start[color] + i) % 3])

    print(*result)

main()
