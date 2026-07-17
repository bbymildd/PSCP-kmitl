"""examscore"""
def main():
    """examscore"""
    num_rabbit = int(input())
    scores = []

    for i in range(num_rabbit):
        scores.append(int(input()))
        
    high = max(scores)
    count = 0
    for score in scores:
        if score == high:
            count += 1
            print(high)
            print(count)

main()
