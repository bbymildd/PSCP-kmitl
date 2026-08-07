"""coffee"""
from decimal import Decimal, ROUND_HALF_UP
def main():
    """coffee"""
    day = int(input())
    add = 0
    sales = []
    for _ in range(day):
        sell = int(input())
        sales.append(sell)
        add += sell
    high = max(sales)
    low = min(sales)
    mean = Decimal(add / day)
    print(add)
    print(high)
    print(low)
    print(mean.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))

main()
