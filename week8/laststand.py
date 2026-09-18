"""lastnum"""
def main():
    """lastnum"""
    number = input()
    number = number.replace("[", "")
    number = number.replace("]", "")
    number = number.split(",")

    for num in number:
        print(int(num) % 10)

main()
