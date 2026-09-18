"""tuple"""
def main():
    """tuple"""
    num = tuple(input().split())
    number = input()
    ans = num.index(number)
    pic = [ans] * num.count(number)

    for _ in range(num.count(number)):
        print(*pic)

main()
