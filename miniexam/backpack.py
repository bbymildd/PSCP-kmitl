"""back"""
def main():
    """pack"""
    item = input()

    if item == "Empty":
        bag = []
    else:
        bag = item.split(",")

    new = input()

    if new == "Stone":
        print("I don't need this!")
        print(bag)
        return

    if len(bag) < 5:
        bag.append(new)
    else:
        bag.pop(0)
        bag.append(new)

    print(bag)

main()
