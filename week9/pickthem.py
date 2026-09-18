"""pickthem"""
import json
def main():
    """pickthem"""
    num = json.loads(input())
    count = 0

    for i in num:
        if not i % 2:
            print(i)
            count += 1

    if not count:
        print("Nope")

main()
