"""charm"""
def main():
    """charm"""
    num = int(input())
    bowls = []

    for _ in range(num):
        bowls.append(int(input()))

    answer = 0

    for bowl in bowls:
        count = bowls.count(bowl)

        if count > answer:
            answer = count

    print(answer)

main()
