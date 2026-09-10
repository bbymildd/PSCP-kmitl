"""rome"""
def main():
    """rome"""
    key = input()
    room = "13"
    sumnum = 0
    mulnum = 1
    for c in key:
        n = int(c)
        i = key.find(c)
        if room == "13" and n > 5:
            room = str(9 + (i >= 4 and i+1 or i))
        sumnum += n
        mulnum *= n
    if key == key[::-1]:
        if int(key[0]) + int(key[4]) > 5:
            room += "1"
        elif int(key[1]) * int(key[3]) > 5:
            room += "2"
        else:
            room += "0"
    else:
        if int(key[0]) // (not int(key[4]) and 1 or int(key[4])) > 5:
            room += "1"
        elif int(key[1]) - int(key[4]) > 5:
            room += "2"
        else:
            room += "0"
    if sumnum > 25:
        room += "1"
    elif mulnum > 55:
        room += "2"
    else:
        room += "0"

    print(room)

main()
