"""divide"""
def main():
    """divide"""
    num = int(input())
    total = 0
    for i in range(1,num + 1):
        if not i % 3 or not i % 5:
            total += i
    print(total)

main()
