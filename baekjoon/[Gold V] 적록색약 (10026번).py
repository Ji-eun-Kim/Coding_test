#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 적록색약: 빨간색=초록색, 파란색 총 2가지색으로
# 일반인: 빨간색, 초록색, 파란색 총 3가지색


# In[20]:


from collections import deque

N= int(input())
graph=[list(input()) for _ in range(N)]

visited=[[False]*N for _ in range(N)]
q=deque()

#일반인, 색맹 count 초기화
three=0
two=0

dx= [1,-1,0,0]
dy= [0,0,1,-1]


def bfs(x,y):
    q.append((x,y))
    visited[x][y]=True
    
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx <N and 0<=ny<N and visited[nx][ny]==False and graph[nx][ny]==graph[x][y]:
                    visited[nx][ny]=True
                    q.append((nx,ny))


                
#모든 좌표 다 돌아다녀보면서 방문하지 않았다면 함수에 넣기                
for i in range(N): #0일 때
    for j in range(N): #0,1,2,3,4 돌아다님
        if visited[i][j]==False:
            bfs(i,j)
            three+=1
            
#적록색약인 경우,
for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            graph[i][j]='G'
            
visited=[[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            bfs(i,j)
            two+=1
    
print(three,two)

