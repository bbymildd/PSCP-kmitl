"""iphone"""
def main():
    """iphone"""
    iphone = {
        "iPhone 13 mini": 25900,
        "iPhone 13": 29900,
        "iPhone 13 Pro": 38900,
        "iPhone 13 Pro Max": 42900
    }
    storage = {
        "128 GB": 0,
        "256 GB": 4000,
        "512 GB": 12000,
        "1 TB": 20000
    }

    iphone13 = input()
    capacity = input()

    if iphone13 not in iphone or capacity not in storage:
        print("Not Available")
    elif capacity == "1 TB" and iphone13 in ("iPhone 13 mini", "iPhone 13"):
        print("Not Available")
    else:
        print(iphone[iphone13] + storage[capacity])

main()
