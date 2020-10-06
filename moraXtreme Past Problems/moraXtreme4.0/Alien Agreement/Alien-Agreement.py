n, m = map(int, input().split())

S = [0] * n
T = [0] * n

for _ in range(m):
    v1, v2 = map(int, input().split())

    if v1 <= n < v2:
        S[v1 - 1] = 1
        T[v2 - n - 1] = 1

    elif v1 > n >= v2:
        S[v2 - n - 1] = 1
        T[v1 - 1] = 1

print(min(sum(S),sum(T)))
