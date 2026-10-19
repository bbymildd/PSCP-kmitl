"""missing"""
def main():
    """missing"""
    num = int(input())
    miss = []
    while True:
        number = int(input())
        if not number:
            break
        miss.append(number)

    for i in range(1,num + 1):
        if i not in miss:
            print(i)

main()
