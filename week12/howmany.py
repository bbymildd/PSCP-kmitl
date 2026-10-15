"""many"""
def main():
    """many"""
    boy = 0
    girl = 0
    total = 0
    while True:
        num = int(input())
        if num < 0:
            break
        if not num % 2:
            girl += 1
        elif num % 2:
            boy += 1
    total = boy + girl
    print(boy, girl, total)

main()
