"""item"""
def main():
    """item"""
    bag = list(input().lower().split())
    have = input()
    see = have.lower()

    if see in bag:
        print(f"{have} is in the list")
    else:
        print(f"{have} is not in the list")

main()
