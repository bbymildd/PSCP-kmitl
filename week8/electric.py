"""electric"""
def main():
    """electric"""
    use = int(input())

    if use > 200:
        more = use - 200
        total = (more * 15) + 2030
    elif 100 < use <= 200:
        more = use - 100
        total = (more * 12) + 830
    elif 50 < use <= 100:
        more = use - 50
        total = (more * 10) + 330
    elif 10 < use <= 50:
        more = use - 10
        total = (more * 7) + 50
    else:
        total = use * 5

    FT = use * 0.5
    print(f"{(total * 1.07) + FT:.1f}")

main()
