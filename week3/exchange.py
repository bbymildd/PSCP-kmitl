"""exchange"""
def main():
    """exchange"""
    money = int(input())

    ten = money // 10
    money = money % 10
    five = money // 5
    money = money % 5
    two = money // 2
    money = money % 2
    one = money // 1
    money = money % 1

    print(f"10 = {ten}")
    print(f"5 = {five}")
    print(f"2 = {two}")
    print(f"1 = {one}")

main()
