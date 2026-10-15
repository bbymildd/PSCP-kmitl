"""nodu"""
def main():
    """nodu"""
    _ = int(input())
    numbers = list(map(int, input().split()))
    nodu = set()
    for number in numbers:
        if numbers.count(number) == 1:
            nodu.add(number)
    print(*sorted(nodu))

main()
