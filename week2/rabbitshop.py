"""rabbit"""
def main():
    """rabbit"""
    num = input()
    num_split = num.split(" ")
    x = int(num_split[0])
    y = int(num_split[1])
    z = int(num_split[2])

    car = x * 10
    cab = y * 25
    tom = z * 3

    print(f"{car + cab + tom}")

main()