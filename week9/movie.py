"""movie"""
def main():
    """movie"""
    name1 = input()
    name2 = input()

    while len(name1) < len(name2):
        name1 += name1[0]

    while len(name2) < len(name1):
        name2 += name2[0]

    result = ""

    for i, char in enumerate(name1):
        if name1[i].lower() in "love" or name2[i].lower() in "love":
            result += "w"
        else:
            result += "$"

    count_w = result.count("w")

    if count_w % 2 == 1:
        max_w = 0
        current_w = 0

        for char in result:
            if char == "w":
                current_w += 1
                if current_w > max_w:
                    max_w = current_w
            else:
                current_w = 0

        result += str(max_w)

    elif "ww" not in result:
        result += "#"

    print(result)

main()
