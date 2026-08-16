"""aeiou"""
def main():
    """aeiou"""
    num = int(input())
    aeiou = ["A","E","I","O","U"]
    nub = 0
    while num:
        font = input().upper()
        if font in aeiou:
            nub += 1
        num -= 1
    print(nub)
main()

# """aeiou"""
# def main():
#     """aeiou"""
#     n = int(input())
#     count = 0

#     for _ in range(n):
#         eng = input().upper()

#         if eng.find("A") != -1:
#             count += 1
#         if eng.find("E") != -1:
#             count += 1
#         if eng.find("I") != -1:
#             count += 1
#         if eng.find("O") != -1:
#             count += 1
#         if eng.find("U") != -1:
#             count += 1

#     print(count)

# main()
