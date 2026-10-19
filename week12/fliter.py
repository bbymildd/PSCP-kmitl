"""fliter"""
import json
def main():
    """fliter"""
    student = json.loads(input())
    must = float(input())
    fliter = [[int(i), j] for i, j in student.items() if j >= must]
    fliter.sort(key=lambda s: s[0])

    if not fliter:
        print("Nope")
    for i,j in fliter:
        if j >= must:
            print(f"{i}\t{j:.2f}")

main()
