"""direct"""
def main():
    """direct"""
    direct = input()

    arrows = {
        "U": [
            "  *   ",
            " ***  ",
            "* * * ",
            "  *   ",
            "  *   "
        ],
        "D": [
            "  *   ",
            "  *   ",
            "* * * ",
            " ***  ",
            "  *   "
        ],
        "L": [
            "  *   ",
            " *    ",
            "***** ",
            " *    ",
            "  *   "
        ],
        "R": [
            "  *   ",
            "   *  ",
            "***** ",
            "   *  ",
            "  *   "
        ]
    }

    direct = [arrows[d] for d in direct]

    for row in range(5):
        print("".join(c[row] for c in direct))

main()
