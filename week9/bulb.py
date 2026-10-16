"""bulb"""
def main():
    """bulb"""
    num = int(input())
    tall = []

    for _ in range(num):
        high = int(input())
        tall.append(high)

    tall.sort()

    total = 0
    h_sum = 0

    for high in tall:
        h_sum += high
        total += h_sum * 2

    print(total)

main()
