"""round"""
def main():
    """round"""
    people, run = map(int, input().split())

    times = []
    for _ in range(people):
        times.append(int(input()))

    fastest = min(times)
    count = 0

    for time in times:
        eliminated = False

        for lap in range(2, run + 1):
            if lap * fastest <= (lap - 1) * time:
                eliminated = True
                break

        if not eliminated:
            count += 1

    print(count)

main()
