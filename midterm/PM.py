"""pm"""
def main():
    """pm"""
    num = int(input())
    day = 0
    peak = 0
    streak = 0
    current = 0
    start = 0
    current_start = 0

    for i in range(1, num + 1):

        pm = int(input())

        if pm > peak:
            peak = pm

        if pm > 50:
            day += 1
            current += 1

            if current == 1:
                current_start = i

            if current >= streak:
                streak = current
                start = current_start

        else:
            current = 0

    if not streak:
        start = 0

    print(f"OVER = {day}")
    print(f"PEAK = {peak}")
    print(f"STREAK = {streak}")
    print(f"START = {start}")

main()
