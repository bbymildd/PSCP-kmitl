"""rabbit"""
def main():
    """rabbit"""
    num = input()
    num_split = num.split(" ")
    wid = int(num_split[0])
    long = int(num_split[1])
    floor = int(num_split[2])

    price = int(input())
    l = ((wid*2)+(long*2))*floor
    print(l)
    print(f"{l*price}")

main()
