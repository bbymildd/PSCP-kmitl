"""ham"""
def main():
    """ham"""
    text1 = input()
    text2 = input()
    count = 0

    for i, char in enumerate(text1):
        if char != text2[i]:
            count += 1
    print(count)

main()
