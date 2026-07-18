"""lowest"""
def main():
    """lowest"""
    num = int(input())
    lowest = int(input())
    for _ in range(num - 1):
        nums = int(input())
        if nums < lowest:
            lowest = nums
    print(lowest)
main()
