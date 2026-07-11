"""quadrant"""
def main():
    """quadrant"""
    x = int(input())
    y = int(input())

    if x > 0:
        if y > 0:
            print("Q1")
        elif y < 0:
            print("Q4")
        elif not y:
            print("X")
    elif x < 0:
        if y > 0:
            print("Q2")
        elif y < 0:
            print("Q3")
        elif not y:
            print("X")
    elif not x:
        if not y:
            print("O")
        elif y > 0 or y < 0:
            print("Y")

main()
