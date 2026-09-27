"""rov"""
def main():
    """rov"""
    game = input()
    point = int(input())

    if game == "Rov" and point >= 2:
        print("GGEZ")
    elif game == "Valorant" and point >= 7:
        print("GGEZ")
    else:
        print("GGWP")

main()
