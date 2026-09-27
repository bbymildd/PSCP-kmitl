"""bus_stop"""
def main():
    """bus_stop"""
    capacity = int(input())
    station = int(input())
    data = []

    for _ in range(station):
        data.append(list(map(int, input().split())))
    data.sort(key=lambda x: x[0])

    bus = []
    count = 0

    for stop in data:
        current = stop[0]
        person_list = stop[1:]

        while current in bus:
            bus.remove(current)
            count += 1

        for person in person_list:
            if person > current and len(bus) < capacity:
                bus.append(person)

    print(count)

main()
