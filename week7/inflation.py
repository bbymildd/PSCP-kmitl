"""inflation"""
def main():
    """inflation"""
    n = input()
    k = int(input())

    n = int(float(n) * 100)

    for _ in range(k):
        n = n * 10381 // 10000

    print(f"{n // 100}.{n % 100:02d}")

main()
