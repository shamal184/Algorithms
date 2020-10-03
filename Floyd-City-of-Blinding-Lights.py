import math

inf = math.inf

n,m = map(int,input().split())

A = []

for i in range(n):
    A.append([inf]*n)
    A[i-1][i-1] = 0


for i in range(m):
    v1, v2, w = map(int,input().split())
    A[v1-1][v2-1] = w


for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])



q = int(input())

for i in range(q):
    v1,v2 = map(int,input().split())
    if A[v1-1][v2-1] == inf:
        print(-1)
    else:
        print(A[v1-1][v2-1])
