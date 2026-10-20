
"""dart"""
def main():
    """Calculate dart score"""
    many = int(input())
    score = 0

    for _ in range(many):
        x, y = map(int, input().split())
        distance = x * x + y * y

        if distance <= 4:
            score += 5
        elif distance <= 16:
            score += 4
        elif distance <= 36:
            score += 3
        elif distance <= 64:
            score += 2
        elif distance <= 100:
            score += 1

    print(score)

main()
