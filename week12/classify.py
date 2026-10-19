"""classify"""
def main():
    """classify"""
    student = []
    used = []
    frac = []
    while True:
        idee = input()
        if idee == "END":
            break
        student.append(idee)
    student = sorted(student)
    check = [d[:4] for d in student]

    for i in student:
        if i[:4] in frac:
            continue
        if i[:2] in used:
            print("--", int(i[2:4]), check.count(i[:4]))
        else:
            print(i[:2], int(i[2:4]), check.count(i[:4]))
        used.append(i[:2])
        frac.append(i[:4])

main()
