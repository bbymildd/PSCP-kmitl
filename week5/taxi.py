"""taxi"""
def main():
    """taxi"""
    mile = int(input())

    if 0 < mile <= 1:
        print("35")
    elif 1 < mile <= 10:
        kilo = 35 + (mile - 1) * 5
        print(kilo)
    else:
        kilos = 35 + 45 + ((mile - 10) * 8)
        print(kilos)
main()
