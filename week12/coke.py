"""coke"""
def main():
    """coke"""
    fullprice = int(input())
    bcap = int(input())
    newprice = int(input())
    bottle = int(input())

    if not bcap:
        print(fullprice * bottle)
        return
    if not bottle:
        print(0)
    else:
        bottle = bottle - 1
        pattern = bottle // bcap
        pattern_left = bottle % bcap
        price_per_set =  (bcap - 1) * fullprice + newprice
        total = fullprice + (pattern * price_per_set) + (pattern_left * fullprice)
        print(total)

main()
