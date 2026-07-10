"""point"""
import math
def main():
    """point"""
    num1 = input()
    num1_split = num1.split(" ")
    x1 = int(num1_split[0])
    y1 = int(num1_split[1])
    z1 = int(num1_split[2])

    num2 = input()
    num2_split = num2.split(" ")
    x2 = int(num2_split[0])
    y2 = int(num2_split[1])
    z2 = int(num2_split[2])

    d = math.sqrt((x1-  x2)**2 + (y1 - y2)**2 + (z1 -z2)**2)
    print(f"{d:.2f}")

main()
