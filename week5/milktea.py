"""Bubble Milk Tea"""
def main():
    """Bubble Milk Tea"""
    cup1 = input().split()
    cup2 = input().split()
    boba = cup1[0]
    b_amount = float(cup1[1])
    tea = cup2[0]
    sweet = int(cup2[1])
    t_amount = float(cup2[2])
    mix = {
        "R" : {1 : 12, 2 : 18, 3 : 25},
        "T" : {1 : 15, 2 : 20, 3 : 30},
        "M" : {1 : 10, 2 : 15, 3 : 20}}
    mix = mix[tea][sweet]

    match boba:
        case "H":
            result = (b_amount * 5) + (mix * t_amount)
        case "O":
            result = (b_amount* 3) + (mix * t_amount)
        case _:
            result = (b_amount* 2) + (mix * t_amount)

    if not result % 1:
        print(int(result))
    else:
        print(result)

main()
