"""longer"""
import math as m
def main():
    """longer"""
    r = float(input())
    a = float(input())
    b = float(input())

    circle = 2 * m.pi * r
    square = (2 * a) + (2 * b)

    if circle > square:
        print("Circle is longer")
        dif = abs(circle - square)
        print(f"{dif:.5f}")
    elif circle < square:
        print("Rectangle is longer")
        dif = abs(circle - square)
        print(f"{dif:.5f}")
    elif circle == square:
        print("Equal")
        print(f"{0:.5f}")

main()
