"""rightarrow"""
def main():
    """rightarrow"""

    width = int(input())
    high = int(input())

    center = high // 2

    for i in range(high):
        space = center - abs(center - i)
        print(" " * space + "*" * width)

main()
