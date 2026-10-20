"""near"""
def main():
    """near"""
    alice = int(input())
    bob = int(input())
    itim = int(input())

    if abs(itim - alice) > abs(itim - bob):
        print(f"Bob {abs(itim - bob)}")
    elif abs(itim - alice) == abs(itim - bob):
        print(f"Sundaes {abs(itim - bob)}")
    else:
        print(f"Alice {abs(itim - alice)}")

main()
