#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
import copy
import sys
input=sys.stdin.readline

N,M= map(int,input().split())
graph=[]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs():
    queue=deque()
    tmp_graph=copy.deepcopy(graph)
    
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j]==2:
                queue.append((i,j))
    
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if tmp_graph[nx][ny]==0:
                    tmp_graph[nx][ny]=2
                    queue.append((nx,ny))
                    
                    
    global answer
    cnt=0
    
    for i in range(N):
        cnt+= tmp_graph[i].count(0) #0인 애들을 다 세어주는 코드
    
    
    #각 경우의 수마다 cnt와 비교해서 더 큰 값을 answer 저장
    #새롭게 cnt가 더 큰 값이 나오게 되면, 기존 answer 와 비교해보고 answer에 업데이트함 
    answer=max(answer,cnt)
    
    

#벽세우기    
#벽이 3개가 되면, 바이러스를 퍼트려 본다
def makeWall(cnt):
    if cnt==3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                makeWall(cnt+1)
                graph[i][j]=0

for i in range(N):
    graph.append(list(map(int,input().split())))
answer=0
makeWall(0)
#초깃값 저장
print(answer)


# In[ ]:




