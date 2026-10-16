"""beast"""
def main():
    """beast"""
    beast = {
        "Spider Demon": 1,
        "Swamp Demon": 2,
        "Arrow Demon": 1,
        "Hand Demon": 2,
        "Drum Demon": 3,
        "Mugen Train": 2,
        "Upper Moon": 3
    }

    queue = list(beast.keys())
    kill = 0
    total = 0

    while kill < 5:
        name = queue.pop(0)
        print(name)

        fail = 0

        while fail < 2:
            answer = int(input())
            total += 1

            if answer == beast[name]:
                print("kill")
                kill += 1
                break

            fail += 1

        if fail == 2:
            print("back")
            queue.append(name)

    print(total)


main()
