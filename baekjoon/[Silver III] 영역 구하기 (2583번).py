#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]

# 박스 채우는 코드
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):  # 0 ~ 3
        for j in range(M - y1 - 1, M - y2 - 1, -1):  # 2, 1까지만
            graph[j][i] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 돌면서 그래프가 0인 경우, 1로 변환하고 size에 +1해서 영역 넓이 구해줌
def bfs(x, y):
    global answer
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                size += 1
    result.append(size)

result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(i, j)

# 영역의 넓이 리스트 안에 집어넣음
result.sort()
print(len(result))  # 영역 개수 출력
for i in result:
    print(i, end=' ')

