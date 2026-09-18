"""diff"""
def main():
    """diff"""
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    for _ in range(n):
        num = int(input())
        a.add(num)
    for _ in range(m):
        mum = int(input())
        b.add(mum)

    ans = list(a-b)
    ans.sort()
    print(*ans)

main()
