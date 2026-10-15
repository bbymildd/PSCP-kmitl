"""hint"""
def main():
    """hint"""

    def check(number, op, value):
        """check condition"""
        if op == ">":
            return number > value
        if op == "<":
            return number < value
        if op == ">=":
            return number >= value
        if op == "<=":
            return number <= value
        if op == "==":
            return number == value
        if op == "!=":
            return number != value
        return False

    one = input()
    two = input()
    three = input()

    one_op, one_num = one.split()
    two_op, two_num = two.split()
    three_op, three_num = three.split()

    one_num = int(one_num)
    two_num = int(two_num)
    three_num = int(three_num)

    for loi in range(10):
        for sib in range(10):
            for nui in range(10):
                if check(nui, one_op, one_num) and \
                    check(sib, two_op, two_num) and \
                    check(loi, three_op, three_num):
                    print(f"{loi}{sib}{nui}")

main()
