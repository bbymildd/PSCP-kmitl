"""sorry"""
def main():
    """sorry"""
    buy = []

    while True:
        menu = input()

        if menu == "End":
            break

        if menu == "Sorry":
            buy.pop()
        else:
            buy.append(menu)

    print(", ".join(buy))

main()
