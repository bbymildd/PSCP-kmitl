"""symbol"""
def main():
    """symbol"""
    sym = 0
    num = int(input())
    for _ in range(num):
        sym = "*"
        sym += 1
        num -= 1
    print(sym)
main()