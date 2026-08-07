"""export"""
def main():
    """export"""
    n = int(input())
    add = 0
    even = 0
    odd = 0
    for _ in range(n):
        num = int(input())
        add += num
        if not num % 2:
            even += 1
        if num % 2:
            odd += 1

    print(f"SUM {add}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")

main()
