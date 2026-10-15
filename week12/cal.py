"""cal"""
def main():
    """cal"""
    fruit = {1:100, 2:120, 3:200, 4:60}
    total = 0
    while True:
        num = int(input())
        if num == 5:
            break
        total += fruit[num]
    print("Bye Bye")
    print(f"Total Calories: {total}")

main()
