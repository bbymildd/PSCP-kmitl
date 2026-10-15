"""bird"""
def main():
    """bird"""
    num_b = int(input())
    b_list = list(map(int, input().split()))
    tall_b = 0

    if num_b == 1:
        print(1)
        return

    for i in range(num_b):
        if not i:
            if b_list[i] > b_list[i + 1]:
                tall_b += 1

        elif i == num_b - 1:
            if b_list[i] > b_list[i - 1]:
                tall_b += 1

        else:
            if b_list[i - 1] < b_list[i] > b_list[i + 1]:
                tall_b += 1

    print(tall_b)

main()
