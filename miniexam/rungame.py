"""run"""
def main():
    """run"""
    try:
        items = input().split()
    except EOFError:
        items = []

    current = 0
    total = 0

    for item in items:
        position = int(item)
        total += abs(position - current)
        current = position

    print(total)

main()
