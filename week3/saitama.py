"""saitama"""
import math as m
def main():
    """saitama"""
    witfloor = int(input())
    situp = int(input())
    looksit = int(input())
    run = int(input())
    w = int(input())
    s = int(input())
    r = int(input())
    l = int(input())

    mw = m.ceil(witfloor / w)
    ms = m.ceil(situp / s)
    ml = m.ceil(looksit / l)
    mr = m.ceil(run / r)

    print(max(mw,ms,ml,mr))

main()
