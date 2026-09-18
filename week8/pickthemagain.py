"""divide"""
def main():
    """divide"""
    number = list(map(int, input().split()))
    found = False

    for num in number[::-1]:
        if not num % 3 or not num % 5:
            print(num)
            found = True

    if not found:
        print("Nope")

main()
