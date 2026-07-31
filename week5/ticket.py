"""ticket"""
def main():
    """ticket"""
    num = input()
    num_split = num.split(" ")
    age = int(num_split[0])
    day = str(num_split[1])

    if day != "Wed":
        if age < 5:
            print("0")
        elif 5 <= age <= 18:
            print("100")
        elif age >= 19:
            print("150")
    elif day == "Wed":
        if age < 5:
            print("0")
        elif 5 <= age <= 18:
            print("50")
        elif age >= 19:
            print("75")

main()
