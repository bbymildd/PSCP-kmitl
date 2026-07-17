"""tiktok"""
def main():
    """tiktok"""
    num = input()
    num_split = num.split(" ")
    r = int(num_split[0])
    x = int(num_split[1])
    y = int(num_split[2])

    d = (x**2) + (y**2)

    if d < r**2:
        print("IN")
    elif d == r**2:
        print("ON")
    else:
        print("OUT")

main()
