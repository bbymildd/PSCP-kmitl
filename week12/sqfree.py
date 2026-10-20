"""sqfree"""
def main():
    """sqfree"""
    num = int(input())
    count = 0

    for i in range(1, num + 1):
        square_free = True

        for j in range(2, int(i ** 0.5) + 1):
            if not i % (j * j):
                square_free = False
                break

        if square_free:
            count += 1

    print(count)

main()
