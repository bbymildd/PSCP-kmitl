"""gun"""
import math as m
def main():
    """gun"""
    lo = int(input())
    far = []

    for _ in range(lo):
        x1, y1 , distance = map(int, input().split())
        far.append((x1, y1, distance))

    x, y, d = far[0]
    target = []

    for dx in range(-d, d + 1):
        dy2 = d**2 - dx**2
        dy = m.sqrt(dy2)

        if dy * dy == dy2:
            target.append((x + dx, y + dy))
            if dy != 0:
                target.append((x + dx, y - dy))

    for tx, ty in target:
        valid = True

        for x, y, d in far:
            if (x - tx)**2 + (y - ty)**2 != d**2:
                valid = False
                break

        if valid:
            print(f"{tx} {ty:.0f}")
            break

main()
