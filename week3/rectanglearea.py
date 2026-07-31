"""rectangle"""
def main():
    """ractangle"""
    x1, y1, wid1, high1 = map(int, input().split())
    x2, y2, wid2, high2 = map(int, input().split())

    left = max(x1, x2)
    right = min(x1 + wid1, x2 + wid2)

    bottom = max(y1, y2)
    top = min(y1 + high1, y2 + high2)

    overlap_width = right - left
    overlap_height = top - bottom

    if overlap_width <= 0 or overlap_height <= 0:
        print("no overlapping")
    else:
        print(overlap_width * overlap_height)

main()
