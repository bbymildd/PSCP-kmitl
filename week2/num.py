"""renum"""
def main():
    """renum"""
    num1 = input()
    sym = input()
    num2 = int(num1[::-1])
    add = int(num1) + num2
    time = int(num1) * num2

    if sym == "+":
        print(f"{num1} + {num2} = {add}")
    else:
        print(f"{num1} * {num2} = {time}")

main()
