"""resistor"""
def main():
    """resistor"""
    onetwo = {
        "Black" : 0, "Brown" : 1, "Red" : 2, "Orange" : 3,
        "Yellow" : 4, "Green" : 5, "Blue" : 6, "Purple" : 7,
        "Grey" : 8, "White" : 9
    }
    three = {
        "Black" : 1, "Brown" : 10, "Red" : 100,
        "Orange" : 10**3, "Yellow" : 10**4, "Green" : 10**5,
        "Blue" : 10**6, "Purple" : 10**7,
        "Gold" : 0.1, "Silver" : 0.01
    }
    four = {
        "Brown" : 0.01, "Red" : 0.02, "Green" : 0.005,
        "Blue" : 0.0025, "Purple" : 0.001, "Grey" : 0.0005,
        "Gold" : 0.05, "Silver" : 0.1
    }
    colors = []
    for _ in range(4):
        color = input()
        colors.append(color)

    if (
        colors[0] in onetwo
        and colors[1] in onetwo
        and colors[2] in three
        and colors[3] in four
    ):
        num = (onetwo[colors[0]] * 10 + onetwo[colors[1]]) * three[colors[2]]
        dif =  four[colors[3]]
        print(f"{num * (1 - dif):.4f}")
        print(f"{num * (1 + dif):.4f}")
    else:
        print("Error")

main()
