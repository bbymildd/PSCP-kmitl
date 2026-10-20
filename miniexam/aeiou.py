"""aeiou"""
def main():
    """aeiou"""
    time = int(input())
    vowel = ["A", "E", "I", "O", "U"]
    used = []
    count = 0

    for _ in range(time):
        font = input().upper()

        if font in vowel:
            count += 1
            if font not in used:
                used.append(font)

    print(count)

    if len(used) == len(vowel):
        print("YES")
    else:
        print("NO")

main()
