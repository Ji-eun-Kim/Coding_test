#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-7562%EB%B2%88-%EB%82%98%EC%9D%B4%ED%8A%B8%EC%9D%98-%EC%9D%B4%EB%8F%99
#이 분꺼 코드는 왜 돌아가고 내 코드는 왜 계속 런타임 에러나
#이유를 못찾겠음 도저히.

from collections import deque
import sys

dx=[-2,-2,-1,1,2,2,1,-1]
dy=[-1,1,2,2,1,-1,-2,-2]


t=int(input())

for _ in range(t):
    N=int(input())
    now=list(map(int,sys.stdin.readline().split()))
    plan=list(map(int,sys.stdin.readline().split()))
    
    graph=[[0]*N for _ in range(N)]
    visited=[[False]*N for _ in range(N)]
    
    queue=deque()
    
    def bfs():  
        queue.append(now)
        visited[now[0]][now[1]]=True
             #now의 x,y 좌표값임
        while queue:
            x,y=queue.popleft()
            
            if x ==plan[0] and y == plan[1]:
                return 0
             
            for i in range(8):
                nx=x+dx[i]
                dy=y+dy[i]
                 
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                
                if nx==plan[0] and ny==plan[1]:
                    visited[nx][ny]=True
                    return graph[x][y]+1
                 
                if visited[nx][ny]==False:
                    queue.append([nx,ny])
                    visited[nx][ny]=True
                    graph[nx][ny]=graph[x][y]+1
                    
    ans=bfs()
    print(ans)
             

