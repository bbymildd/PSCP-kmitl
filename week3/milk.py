"""milk"""
def main():
    """milk"""
    priceper = int(input())
    cap = int(input())
    milk = int(input())
    money = int(input())

    if not cap:
        full = money // priceper
        print(full)
        return
    if not money:
        print("0")
    else:
        while 