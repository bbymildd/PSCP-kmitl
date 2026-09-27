"""smart"""
def main():
    """trash"""
    trash = int(input())
    for _ in range(trash):
        binn = []
        plastic, can, glass =  map(float, input().split())
        total = plastic + can + glass
        binn.append(f"{total:.1f}")
        if total > 50:
            binn.append("Overloaded")
        if plastic > 20:
            binn.append("Check Type Plastic")
        if can > 20:
            binn.append("Check Type Can")
        if glass > 20:
            binn.append("Check Type Glass")
        print(", ".join(binn))
main()
