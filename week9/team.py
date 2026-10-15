
"""team"""
def main():
    """team"""
    team, mem = map(int, input().split())

    if team < 1 or team > 10 or mem < 1 or mem > 20:
        print("Data Incorrect")
        return

    a_point = []
    m_point = []
    total = 0

    for i in range(team):
        num = list(map(int, input().split()))
        total += sum(num)
        aver = sum(num) / mem
        a_point.append(aver)
        m = max(num)
        m_point.append(m)

    for i in range(team):
        print(
            f"Team {i + 1}: Average = {a_point[i]:.2f}, "
            f"Max = {m_point[i]}"
        )

    print(f"Total Score of All Teams = {total}")


main()
