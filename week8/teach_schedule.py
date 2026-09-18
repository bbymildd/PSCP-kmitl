"""schedule"""
def main():
    """schedule"""
    teach = int(input())
    time = int(input())
    total_min = teach * time
    hour = total_min // 60
    minute = total_min - (hour * 60)
    if not total_min:
        print("No teaching")
    elif total_min <= 59:
        print(f"{minute} minute")
    elif total_min > 59 and not minute:
        print(f"{hour} hours")
    else:
        print(f"{hour} hours {minute} minute")

main()
