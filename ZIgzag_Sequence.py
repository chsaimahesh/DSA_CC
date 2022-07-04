def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    lis_1 = a[:mid]
    lis_2 = a[n-1:mid-1:-1]
    lis_1.extend(lis_2)
    print(lis_1)
    return


test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


