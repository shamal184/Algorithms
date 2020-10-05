import collections

n = int(input())

for _ in range(n):
    ve, e, lib, rd = map(int, input().split())
    adj = [[] for i in range(ve)]
    for i in range(e):
        lst = list(map(int, input().split()))
        lst.sort()
        v1 = lst[0]
        v2 = lst[1]
        adj[v1 - 1].append(v2)
        adj[v2 - 1].append(v1)
    v = [i+1 for i in range(ve)]
    s = v[0]

    # parent = {s:None}
    parent = {}


    def DFS_Visit(adj, s):
        # global parent
        for v in adj[s - 1]:
            if v not in parent:
                parent[v] = s
                DFS_Visit(adj, v)


    def DFS(v, adj):
        for s in v:
            if s not in parent:
                parent[s] = None
                DFS_Visit(adj, s)


    DFS(v, adj)
    DFS_Visit(adj, s)
    parent = collections.OrderedDict(sorted(parent.items()))
    #print(parent)


    def get_key(val):
        for key, value in parent.items():
            if val == value:
                return key


    trees = [i for i in parent if parent[i] == None]
    trees2 = []
    #print(trees)
    j=0

    for i in parent:
        if parent[i] == None and i!=1:
            trees2.append(j)
            j=0

        else:
            if i!=1:
                j+=1

            if i == ve:
                trees2.append(j)

    #print(trees2)

    sum1 = (lib * len(trees)) + (rd * sum(trees2))
    sum2 = (lib * ve)

    print(min(sum1, sum2))
