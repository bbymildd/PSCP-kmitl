"""cal"""
def main():
    """cal"""
    amount = int(input())
    if amount == 1:
        print("1")
        return
    num_click = 0

    for i in range(1, amount+1):
        num_click += len(str(i))
    print(num_click+amount)

main()
