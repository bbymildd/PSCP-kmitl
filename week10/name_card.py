"""card"""
def main():
    """card"""
    data = input().upper()
    f_card = {"A": "Ace", "J":"Jack", "Q":"Queen", "K":"King"}
    b_card = {"D":"Diamonds", "H":"Hearts", "S":"Spades", "C":"Clubs"}
    if data[0] == "1":
        print(f"10 of {b_card[data[-1]]}")
    elif data[0].isnumeric():
        print(f"{data[0]} of {b_card[data[-1]]}")
    else:
        print(f"{f_card[data[0]]} of {b_card[data[-1]]}")

main()
