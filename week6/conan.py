"""conan"""
def main():
    """conan"""
    text = input()
    k = int(input())

    result = ""

    for char in text:
        new_char = chr((ord(char) - ord("a") + k) % 26 + ord("a"))
        result += new_char

    print(result)

main()
