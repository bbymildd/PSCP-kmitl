"""array"""
def main():
    """array"""
    array = []

    for i in range(5):
        row = list(map(int, input().split()))
        array.append(row)

    stuck_row = -1
    stuck_column = -1

    for i in range(5):
        total = sum(array[i])

        if total % 2:
            stuck_row = i

    for j in range(5):
        total = 0

        for i in range(5):
            total += array[i][j]

        if total % 2:
            stuck_column = j

    print(stuck_row, stuck_column)

main()
