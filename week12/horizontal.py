"""horizontal"""
def main():
    """horizontal"""
    name = list(input())
    used = []
    name.sort(key=lambda n: (n.isupper(), ord(n)))
    for i in name:
        if i not in used:
            group = name.count(i) // 5
            remain = name.count(i) % 5
            if not name.count(i) % 5:
                group -= 1
                remain = 5
            print(f"{i} : {'-----|' * group + '-' * remain}")
            used.append(i)
main()
