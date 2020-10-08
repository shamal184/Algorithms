visited = []
EulerTourNodes = []
EulerTourDic = {}
EulerTourIndxs = []
EulerTourDicIndex = {}
index = 0


def EulerTour(node, adj):
    global index
    visited.append(node)
    EulerTourNodes.append(node)
    EulerTourDic[node] = index
    EulerTourDicIndex[index] = node
    EulerTourIndxs.append(index)
    index += 1

    for u in adj[node]:
        if u not in visited:
            EulerTour(u, adj)
            EulerTourNodes.append(node)
            EulerTourIndxs.append(EulerTourDic[node])
            #index += 1


if __name__ == '__main__':
    n, q = map(int, input().split())

    colors = list(map(int, input().split()))

    parentArr = list(map(int, input().split()))
    parentArr.insert(0, 0)
    adj = [[] for i in range(n + 1)]

    for i in range(1, n):
        adj[i + 1].insert(0, parentArr[i])
        adj[parentArr[i]].insert(0, i + 1)

    EulerTour(1, adj)

    print(visited)
    print(EulerTourDic)
    print(EulerTourDicIndex)
    print(EulerTourNodes)
    print(EulerTourIndxs)
    print(adj)
