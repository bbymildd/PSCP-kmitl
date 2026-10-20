"""squid"""
def main():
    """game"""
    power = []
    for _ in range(20):
        force = int(input())
        power.append(force)
    A = sum(power[:10])
    B = sum(power[10:20])
    if A > B:
        print("B")
    elif A == B:
        print("AB")
    else:
        print("A")

main()
