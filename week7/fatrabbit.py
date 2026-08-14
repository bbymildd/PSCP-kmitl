"""fatrabbit"""
def main():
    """FATRABBIT"""
    n = int(input())
    nub = 0
    fat = 0
    fat_name = ""

    for _ in range(n):
        name, num = input().split()
        num = int(num)

        if num > 15:
            nub += 1

        if num > fat:
            fat = num
            fat_name = name

    print(nub)
    print(fat_name)

main()
