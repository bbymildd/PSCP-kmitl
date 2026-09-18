"""saibox"""
def main():
    """saibox"""
    b_wid, b_long, A_start, A_stop = map(int, input().split())
    minimum = b_wid * b_long

    for A in range(A_start, A_stop + 1):
        waste = (b_wid % A) * (b_long % A)

        if waste < minimum:
            minimum = waste

    print(minimum)

main()
