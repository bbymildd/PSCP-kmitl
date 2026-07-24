"""test"""
def main():
    """test"""
    Test = int(input())
    mid = int(input())
    fin = int(input())

    total = Test + mid + fin
    if Test < 5 or mid < 20 or fin < 25:
        print("fail")
        return
    if total >= 50:
        print("pass")
    elif total < 50:
        print("fail")
main()
