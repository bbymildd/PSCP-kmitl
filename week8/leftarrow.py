"""leftarrow"""
def main():
    """leftarrow"""

    width = int(input())
    high = int(input())

    center = high // 2

    for i in range(high):
        space = abs(center - i)
        print(" " * space + "*" * width)

main()
