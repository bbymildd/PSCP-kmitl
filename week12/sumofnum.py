"""num"""
def main():
    """num"""
    goal = int(input())
    total = 0
    while True:
        number = int(input())
        if number == -1:
            break

        total += number

        if total == goal:
            break
    print(total)

main()
