"""pro"""
import math as m
def main():
    """pro"""
    pen, book, color = map(int, input().split())
    pens = pen * 25
    books = book * 40
    colors = color * 55
    if pen + book + color >= 3:
        dis = (pens + books + colors) * 0.1
        total = (pens + books + colors) - dis
        print(m.floor(total))
    else:
        total = pens + books + colors
        print(m.floor(total))
main()
