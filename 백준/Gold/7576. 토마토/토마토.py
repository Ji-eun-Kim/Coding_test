from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]


dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N:
                if graph[nx][ny]==0:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
 
queue = deque()
for j in range(N):
    for i in range(M):
        if graph[i][j] ==1:
            queue.append((i,j))

bfs()  

 
ans = 0            
#bfs 끝내고    
for i in graph:
    for j in i:
        #최종 그래프에 0이 있는 경우, -1 출력
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))

print(ans-1)