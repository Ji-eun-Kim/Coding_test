from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(''.join(input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == graph[x][y]:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                         
        
visited = [[0]*(N) for _ in range(N)]
cnt1=0
for j in range(N):
    for i in range(N):
        if visited[i][j] == 0:
            bfs(i,j,visited)
            cnt1+=1

for j in range(N):
    for i in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited2= [[0]*(N) for _ in range(N)]
cnt2 =0 
for j in range(N):
    for i in range(N):
        if visited2[i][j] == 0:
            bfs(i,j,visited2)
            cnt2+=1          
            
print(cnt1, cnt2)