h,w = map(int,input().split())

i = []

for _ in range(h):
    lst = list(map(int,input().split()))
    i.append(lst)

#print(i)

area = (h*w)*2
#print(area)

for j in i:
    area += j[0]+j[-1]
    for x in range(len(j)-1):
        area += abs(j[x]-j[x+1])

#print(area)

for k in range(w):
    area += i[0][k] + i[-1][k]
    #print(area)
    for x in range(h-1):
        area += abs(i[x][k] - i[x+1][k])



print(area)
