t = int(input())

for _ in range(t):
    
    n,e = map(int,input().split())
    adj = [[] for i in range(n)]
    for i in range(e):
        v1,v2 = map(int,input().split())
        adj[v1-1].append(v2)
        adj[v2-1].append(v1)

    nulls = [j for j in range(n) if adj[j] == []]
    #print(nulls)
    s = int(input())
    #print(adj)
    level = {s:0}
    for k in range(len(nulls)):
        level[nulls[k]+1] = 0

    i = 1
    front = [s]

    while front:
        next = []

        for u in front:
            for v in adj[u-1]:
                if v not in level:
                    level[v] = i
                    next.append(v)
        front = next
        i+=1

    for i in range(n):
        if i+1 not in level:
            level[i+1] = 0

    #print(level)
    d = []
    for i in range(1,len(level)+1):
        if i == s:
            continue

        elif level[i] == 0:
            d.append(-1)

        else:
            d.append(level[i]*6)

    print(*d)

