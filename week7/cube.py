"""cube"""
def main():
    """cube"""
    gu = int(input())
    cube = int(input())

    if gu > 6 or gu < 1 or cube > 6 or cube < 1:
        print("Invalid")
    elif gu == cube:
        print("Correct!")
    else:
        print("Wrong!")

main()
