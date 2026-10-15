"""easy"""
def main():
    """easy"""
    data = input()

    for letter in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
        count = data.count(letter)
        if count > 0:
            print(letter, "=", count)

main()
