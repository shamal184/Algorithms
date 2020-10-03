import math

inf = math.inf


def minDist(dist, que):
    min1 = inf
    min_index = None

    for v in range(len(dist)):
        if que[v] == False and dist[v] <= min1:
            min1 = dist[v]
            min_index = v

    return min_index


def dijsktra(a_matrix, src, n):
    dist = [inf] * n
    que = [False] * n

    dist[src - 1] = 0

    for x in range(n - 1):
        u = minDist(dist, que)

        que[u] = True

        for v in range(n):
            if a_matrix[u][v] != 0 and dist[v] > dist[u] + a_matrix[u][v]:
                dist[v] = dist[u] + a_matrix[u][v]

    for j in dist:
        if j == inf:
            print(-1, end=" ")

        elif j == 0:
            continue

        else:
            print(j, end=" ")


t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    a_matrix = []

    for j in range(n):
        a_matrix.append([0] * n)

    for j in range(m):
        v1, v2, w = map(int, input().split())
        a_matrix[v1 - 1][v2 - 1] = w
        a_matrix[v2 - 1][v1 - 1] = w

    src = int(input())
    dijsktra(a_matrix, src, n)
    print(" ")
