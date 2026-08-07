"""pass"""
def main():
    """pass"""
    num = int(input())
    add = 0
    passed = True

    for _ in range(num):
        subject = int(input())
        add += subject
        if subject < 50:
            passed = False

    mean = add / num
    print(f"{mean:.1f}")
    if passed and mean >= 60:
        print("PASS")
    else:
        print("FAIL")

main()
