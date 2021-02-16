def getMissingNo(l):
    n = len(l)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(l)
    return total - sum_of_A
n = int(input())
l = [int(i) for i in input().split()]
print(int(getMissingNo(l)))
    