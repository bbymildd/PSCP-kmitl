"""new"""
def main():
    """flu"""
    row, col = map(int, input().split())
    r_row, r_col = map(int, input().split())
    many = int(input())

    city = [[0] * col for _ in range(row)]

    for _ in range(many):
        f_row, f_col = map(int, input().split())

        for i in range(max(0, f_row - 2), min(row, f_row + 3)):
            for j in range(max(0, f_col - 2), min(col, f_col + 3)):
                distance = max(abs(i - f_row), abs(j - f_col))

                if not distance:
                    city[i][j] = max(city[i][j], 100)
                elif distance == 1:
                    city[i][j] = max(city[i][j], 60)
                elif distance == 2:
                    city[i][j] = max(city[i][j], 20)

    safe = 0
    for i in range(row):
        for j in range(col):
            if not city[i][j]:
                safe += 1

    print(safe)
    print(f"{city[r_row][r_col]}%")

main()
