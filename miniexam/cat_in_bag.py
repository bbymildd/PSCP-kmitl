"""cat"""
def main():
    """cat"""
    bag = []
    while True:
        name = input()
        if name == "-1":
            break
        if "cat" in name.lower():
            bag.append(name.lower())

    print(f"The number of cat in bag {len(bag)}")
    print(f"List of cat {bag}")

main()
