"""aeiou"""
def main():
    """aeiou"""
    text = input().lower()
    a = text.count("a")
    e = text.count("e")
    i = text.count("i")
    o = text.count("o")
    u = text.count("u")

    add = a + e + i + o + u
    print(add)

main()
