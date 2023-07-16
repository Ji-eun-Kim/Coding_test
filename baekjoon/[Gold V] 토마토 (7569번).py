#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

m,n,h=map(int,input().split())
graph=[[list(map(int,input().split())) for i in range(n)] for depth in range(h)]

dx=[-1,1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,-1,1]
queue=deque()

def bfs():
    while queue:
        z,x,y=queue.popleft()
        
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny]==0:
                    graph[nz][nx][ny]=graph[z][x][y]+1 #날짜업데이트용
                    queue.append([nz,nx,ny])

#정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토
#모든 행렬을 다 돌아봄
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1: #익은 토마토가 있다면
                queue.append([i,j,k]) #queue에 해당 값을 넣어라
bfs()
answer=1
result=-1 #초깃값 설정

#모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 
#토마토가 모두 익지는 못하는 상황이면 -1을 출력
for i in graph:
    for j in i:
        for k in j:
            if k==0: #만약 완성된 그래프를 보다가 0이 있는 경우, answer을 임시로 0 저장
                answer=0
            
            #행렬 돌아다니면서, 결국 가장 마지막 값이 가장 큰 값이될거고,
            #그 말은 즉, 해당 input에서의 최소 일수일 것임.
            result=max(result,k)
            
if answer==0:
    print(-1)
elif result==1:
    print(0) #모두 익지 못하는 상황
else:
    print(result-1)
    #행렬을 보면서 1인 토마토를 기준으로 퍼뜨릴텐데,
    #1로 나타나 있는 해당 행렬 토마토에 +1(날짜)를 더해주기 때문에, -1을 해줘야함
    #토마토에 1로 나타나있는 것과 날짜+1의 개념은 다르기 때문이다.


# In[ ]:




