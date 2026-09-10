"""tri"""
def main():
    """tri"""
    a = int(input())
    b = int(input())
    c = int(input())

    A = a ** 2
    B = b ** 2
    C = c ** 2

    if not a or not b or not c :
        print("NOT A TRIANGLE")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("NOT A TRIANGLE")
    elif a == b and b == c:
        print("EQUILATERAL")
    elif A == B + C or B == A + C or C == A + B:
        print("RIGHT TRIANGLE")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")

main()
