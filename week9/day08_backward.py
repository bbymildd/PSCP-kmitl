"""day"""
def main():
    """day"""
    all_data = []

    while True:
        data = input()

        if data == "NULL":
            break

        all_data.append(data)

    for i in range(len(all_data) - 1, -1, -1):
        print(all_data[i])

main()
