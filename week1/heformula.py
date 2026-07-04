"""formula"""
def main():
    """formula"""
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a + b + c)/2

    if (s - a) >= 0 and (s - b) >= 0 and (s-c) >= 0:
        area = (s*(s-a)*(s-b)*(s-c))**(1/2)
        print(f"{area:.3f}")

main()
