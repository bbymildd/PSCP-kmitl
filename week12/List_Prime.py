"""prime"""
def main():
    """prime"""
    num = int(input())
    prime = []

    for i in range(2, num + 1):
        is_prime = True

        j = 2
        while j * j <= i:
            if not i % j:
                is_prime = False
                break
            j += 1

        if is_prime:
            prime.append(i)

    if 2 <= num == prime[-1]:
        print("Yes")
        print(*prime)
    else:
        print("No")

main()
