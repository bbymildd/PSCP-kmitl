"""pod"""
def main():
    """pod"""
    num = input().split(" ")
    n = int(num[0])
    k = int(num[1])
    pod = []
    for i in range(n):
        nums = int(input())
        if nums not in pod:
             