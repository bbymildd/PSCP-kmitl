"""stats"""
def main():
    """stats"""
    n = int(input())
    num_min = 2e10
    num_max = -2e10
    total = 0
    for _ in range(n):
        num = int(input())
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num
        total += num
    avg = total / n
    print(f"MIN: {num_min:.3f}")
    print(f"MAX: {num_max:.3f}")
    print(f"AVG: {avg:.3f}")

main()
