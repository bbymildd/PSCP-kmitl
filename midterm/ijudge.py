"""ijudge"""
def main():
    """ijudge"""
    link = input()
    prefix = "https://ijudge.it.kmitl.ac.th/problems/"

    if link.startswith(prefix):
        number = link[len(prefix):]

        if number.endswith("/"):
            number = number[:-1]

        if len(number) == 4 and number.isdigit():
            if number[0] in "0123":
                print(number[0], "STAR")
            else:
                print("INVALID")
        else:
            print("INVALID")
    else:
        print("INVALID")

main()
