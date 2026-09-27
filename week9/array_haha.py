"""array"""
def main():
    """array"""
    number = []

    for i in range(1, 4):
        data = int(input())
        number.append(data)
        print(f"Input number {i} stored.")

    while True:
        num = int(input())

        if not num:
            break

        if num == 1:
            print("Original order:", *number)

        elif num == 2:
            print("Descending order:", *sorted(number, reverse=True))

        else:
            print("Ascending order:", *sorted(number))

main()
