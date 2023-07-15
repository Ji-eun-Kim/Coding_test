#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

m,n= map(int,input().split())

graph= [list(map(int,input().split())) for _ in range(n)]

queue=deque([])

dx=[-1,1,0,0]
dy=[0,0,1,-1]

res=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])
            
def bfs():
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx,ny= dx[i]+x, dy[i]+y
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                #기존 좌표에 값을 누적해서 더해주는 방식으로 함
                queue.append([nx,ny])
                
bfs()

for i in graph:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    res=max(res,max(i))

#첫 시작이 1이기 때문에, 1을 빼줘야 함
print(res-1)

