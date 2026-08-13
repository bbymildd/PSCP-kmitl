"""pod"""
def main():
    """pod"""
    n, k = map(int, input().split())

    queue = [0] * k

    for _ in range(n):
        line = int(input())
        queue[line - 1] += 1

    row = min(queue)
    remain = n - row * k

    print(remain)


main()
