"""storage"""
def add(stock, name, amount):
    """storage"""
    if name not in stock:
        stock[name] = 0
    stock[name] += amount

def remove(stock, name, amount):
    """storage"""
    if name not in stock or stock[name] < amount:
        stock[name] = 0
        print(f"Not enough stock for {name}")
    else:
        stock[name] -= amount

def check(stock):
    """storage"""
    found = False
    for name in sorted(stock):
        if stock[name] < 5:
            print(name)
            found = True
    if not found:
        print("All stocks are sufficient")

def result(stock):
    """storage"""
    for name in sorted(stock):
        print(f"{name}: {stock[name]}")

def main():
    """storage"""
    storage = {}
    while True:
        fruit = input().split()

        if fruit[0] == "END":
            break

        if fruit[0] == "ADD":
            add(storage, fruit[1], int(fruit[2]))
        elif fruit[0] == "REMOVE":
            remove(storage, fruit[1], int(fruit[2]))
        elif fruit[0] == "CHECK":
            check(storage)
        elif fruit[0] == "REPORT":
            result(storage)

main()
