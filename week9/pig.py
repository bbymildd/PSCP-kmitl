"""pig"""
def main():
    """pig"""
    pair = int(input())
    nums = list(map(int, input().split()))
    num_max = []
    total = 0

    for i in range(0, pair * 2, 2):
        first = nums[i]
        second = nums[i + 1]

        if first > second:
            value = first
        else:
            value = second

        num_max.append(value)
        total += value

    if pair == 1:
        print(total)
    else:
        print(" + ".join(map(str, num_max)), "=", total)

main()
