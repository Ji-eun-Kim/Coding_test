#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#bfs while 문 + deque 사용
from collections import deque
import sys
input=sys.stdin.readline


dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,-1,1,1,-1]

def bfs(x,y):
    graph[x][y]=0
    q=deque()
    q.append([x,y])
    
    while q:
        x,y= q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append([nx,ny])
while True:
    w,h= map(int,input().split())
    if w== 0 and h==0:
        break
    graph=[]
    count=0
    for _ in range(h): #높이 만큼 반복
        graph.append(list(map(int,input().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                count+=1
    print(count)


# In[ ]:


#dfs 재귀함수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)



dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,-1,1,1,-1]

def dfs(x,y):
    graph[x][y]=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
            dfs(nx,ny)

while True:
    w,h= map(int,input().split())
    if w== 0 and h==0:
        break
    graph=[]
    count=0
    for _ in range(h): #높이 만큼 반복
        graph.append(list(map(int,input().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)


# In[ ]:




