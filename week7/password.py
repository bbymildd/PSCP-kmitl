"""password"""
def main():
    """password"""
    long = int(input())
    pass1 = input()
    pass2 = input()

    wrong = 0

    for i in range(long):
        if int(pass1[i]) + int(pass2[i]) != 9:
            wrong += 1

    if not wrong :
        print("YES")
    else:
        print("NO", wrong)

main()
