"""present"""
def main():
    """present"""
    num = input()
    num_split = num.split(" ")
    radius = float(num_split[0])
    tall = float(num_split[1])
    glue = float(num_split[2])

    cir = 2 * 3.14 * radius

    long = cir + glue
    width =  (2 * radius) + tall

    print(f"{width:.2f} {long:.2f}")

main()
