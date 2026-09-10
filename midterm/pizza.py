"""pizza"""
import math as m
def main():
    """pizza"""
    mem = int(input())
    piece = int(input())
    tray = int(input())

    want = mem * piece
    order = m.ceil(want / tray)
    left = (order*tray) - want

    print(want)
    print(order)
    print(left)

main()
