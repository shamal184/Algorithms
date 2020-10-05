n = int(input())
lst = [[] for i in range(n)]

for i in range(n):
    x,y = map(str,input().split())
    lst[i].append(int(x))
    lst[i].append(y)

for i in range(int(n/2)):
    lst[i][1] = '-'

min1 = min(lst)[0]
max1 = max(lst)[0]

lst2 = [[] for i in range(min1,max1+1)]

for i in range(n):
    lst2[lst[i][0]].append(lst[i][1])
concat_list = [j for i in lst2 for j in i]
print(*concat_list)


