"""examscore"""
def main():
    """examscore"""
    num_rabbit = int(input())

    highest = int(input())
    count = 1

    for _ in range(num_rabbit - 1):
        x = int(input())
        if x > highest:
            highest = x
            count = 1
        elif x == highest:
            count += 1

    print(highest)
    print(count)

main()
