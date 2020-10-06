import math

inf = math.inf

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
        break

    arr = [inf] * (n+1)
    arr[0] = 0
    arr[1] = 1

    for i in range(1,n+1):
        j = 1
        while j*j <= i:
            arr[i] = min(arr[i], arr[i - (j*j)] + 1)
            j += 1

    print(arr[n])
