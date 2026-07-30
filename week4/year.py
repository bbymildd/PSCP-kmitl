"""year"""
def main():
    """year"""
    yer = int(input())

    if yer > 1582 and not yer % 4:
        if not yer % 100 and not yer % 400:
            print("yes")
        elif not yer % 100:
            print("no")
    elif yer < 1582 and not yer % 4:
        print("yes")
    else:
        print("no")
main()
