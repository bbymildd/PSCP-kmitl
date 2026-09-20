"""noddle"""
def main():
    """noddle"""
    sell = int(input())
    buy = int(input())

    if sell == buy:
        print("Good!")
    elif buy < sell:
        print("Need more cash!")
    else:
        print(abs(buy-sell))

main()
