"""water"""
def main():
    """water"""
    temp = int(input())
    font = input().lower()

    if font == "c":
        if temp <= 0:
            print("solid")
        elif 0 < temp < 100:
            print("liquid")
        else:
            print("gas")
    elif font == "f":
        if temp <= 32:
            print("solid")
        elif 32 < temp < 212:
            print("liquid")
        else:
            print("gas")
main()
