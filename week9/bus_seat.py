"""busseat"""
def main():
    """busseat"""
    seat_inrow = int(input())
    row = int(input())
    seat = int(input())

    for i in range(seat_inrow - 1, -1, -1):
        bus = []
        for j in range(row):
            number = i + (j * seat_inrow) + 1

            if number == seat:
                bus.append("XX")
            else:
                bus.append(f"{number:02d}")

        print(" ".join(bus))

        if not i % 2 and i:
            print()

main()
