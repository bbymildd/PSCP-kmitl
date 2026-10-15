
"""menu"""
def main():
    """menu"""
    menu = []

    while True:
        food = input()

        if food == "DONE":
            break

        if food == "CLOSED":
            menu.clear()
            break

        if food == "SOMETHING'S WRONG":
            menu.clear()
            continue

        if food.startswith("Can't do: "):
            foodd = food.replace("Can't do: ", "", 1)
            if foodd in menu:
                menu.remove(foodd)
            continue

        name, number = food.rsplit(" #", 1)

        if number == "N":
            menu.append(name)
        else:
            menu.insert(int(number) - 1, name)

    print(f"Full Course: {menu} Reversed: {menu[::-1]}")

main()
