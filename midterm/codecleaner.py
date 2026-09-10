"""codecleaner"""
def main():
    """codecleaner"""
    data = input()
    code = ""
    let = 0
    dig = 0

    for char in data:
        if char.isalpha():
            code += char.upper()
            let += 1

        elif char.isdigit():
            code += char
            dig += 1

        else:
            if not code or code[-1] != "-":
                code += "-"

    code = code.strip("-")

    if not code:
        code = "NONE"

    print(f"CODE = {code}")
    print(f"LETTERS = {let}")
    print(f"DIGITS = {dig}")


main()
