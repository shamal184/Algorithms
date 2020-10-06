def maximumArea(h, n):
    stack = []

    maxArea = 0
    area = 0
    i = 0

    while i < n:
        if len(stack) == 0 or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1

        else:
            top = stack.pop()

            if len(stack) == 0:
                area = h[top] * i

            else:
                area = h[top] * (i - stack[-1] - 1)

            if area > maxArea:
                maxArea = area

    while len(stack) != 0:
        top = stack.pop()
        if len(stack) == 0:
            area = h[top] * i

        else:
            area = h[top] * (i - stack[-1] - 1)

        if area > maxArea:
            maxArea = area

    print(maxArea)


t = int(input())

for x in range(t):
    h, w = map(int, input().split())

    matrix = []
    his = []

    for i in range(h):
        row = list(map(int, input().split()))
        if i == 0:
            his = [1 - j for j in row]

        else:
            for j in range(w):
                if row[j] == 0:
                    his[j] += 1

                else:
                    his[j] = 0

    maximumArea(his,w)
