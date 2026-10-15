"""rabbit"""
def main():
    """rabbit"""
    talk = input().lower()
    n = len(talk)
    if all(letter in "it" for letter in talk):
        return print(f"unknown {n}")

    i, max_a = 0, 0

    while i < n:
        if talk[i] == "r":
            if i + 1 >= n:
                return print(f"no {i}")
            if talk[i + 1] != "a":
                return print(f"no {i + 1}")
            start = i + 1
            i += 1
            while i < n and talk[i] == "a":
                i += 1
            max_a = max(max_a, i - start)

        elif talk[i] == "b":
            if i + 1 >= n:
                return print(f"no {i}")
            if talk[i + 1] not in "it":
                return print(f"no {i + 1}")
            i += 1

            while i < n and talk[i] in "it":
                i += 1

        elif talk[i] in "it":
            i += 1

        else:
            return print(f"no {i}")

    return print(f"yes {max_a}")

main()
