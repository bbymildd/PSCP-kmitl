"""fizzbuzz"""
def main():
    """fizzbuzz"""
    line = int(input())
    for i in range(1,line+1):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 5 and i % 3 > 0:
            print("Buzz")
        elif not i % 3 and i % 5 > 0:
            print("Fizz")
        else:
            print(i)

main()
