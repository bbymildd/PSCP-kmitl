"""sum"""
def main():
    """sum"""
    num = int(input())
    total = []
    for _ in range(num):
        n1 = int(input())
        n2 = int(input())

        maximum = max(n1, n2)
        total.append(maximum)

    if num == 1:
        print(total[0])
    else:
        print(" + ".join(map(str, total)), "=", sum(total))

main()
