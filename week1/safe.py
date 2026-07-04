"""safe"""
def main():
    """safe"""
    font = input()
    num = input()

    if font == "H" and num == "4567":
        print("safe unlocked")
    elif font == "H":
        print("safe locked - change digit")
    elif num == "4567":
        print("safe locked - change char")
    else:
        print("safe locked")

main()
