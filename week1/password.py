"""key"""
def main():
    """key"""
    name = input()
    sur = input()
    year = input()

    if len(name) >= 5 and len(sur) >= 5:
        print(f"{name[:2]}{sur[-1]}{year[-1]}")
    else:
        print(f"{name[0]}{year}{sur[-1]}")

main()
