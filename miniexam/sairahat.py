"""sairahat"""
def main():
    """sairahat"""
    data = input()

    if data[:4] == "6807":
        if "0001" <= data[4:8] <= "0328":
            print("Yes")
        else:
            print("No")
    else:
        print("No")

main()
