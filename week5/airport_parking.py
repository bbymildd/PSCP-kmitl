"""parking"""
import math as m
def main():
    """parking"""
    time_in = input()
    time_out = input()

    hour_in, minute_in = map(int, time_in.split("."))
    hour_out, minute_out = map(int, time_out.split("."))
    if not (0 <= hour_in <= 23 and 0 <= minute_in <= 59):
        print("ERROR")
        return
    if not (0 <= hour_out <= 23 and 0 <= minute_out <= 59):
        print("ERROR")
        return
    in_min = hour_in * 60 + minute_in
    out_min = hour_out * 60 + minute_out
    minute = out_min - in_min
    if minute < 0:
        print("ERROR")
        return
    if minute <= 15:
        print("FREE")
        return

    total = m.ceil(minute / 60)
    if total <= 1:
        print("25")
    elif total <= 2:
        print("50")
    elif total <= 3:
        print("80")
    elif total <= 4:
        print("110")
    elif total <= 5:
        print("145")
    elif total <= 6:
        print("180")
    else:
        print("250")

main()
