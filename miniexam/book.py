"""book"""
def main():
    """book"""
    shelf = list(input().split())
    book = input()

    if book in shelf:
        shelf.remove(book)
        print(*shelf)
    else:
        print("There are no book with that name on this shelf")

main()
