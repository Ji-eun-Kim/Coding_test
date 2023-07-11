#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

N=int(input())
graph=[]
maxNum=0 #비가 잠기는 최고 높이값을 초기화

#5번 반복
for i in range(N):
    #빈 graph에 값들을 채워줌
    graph.append(list(map(int,input().split())))
    #N번 반복해서
    for j in range(N):
        if graph[i][j]>maxNum: #maxNum보다 더 큰 값. 즉, 비가 잠기는 최고 높이를 업데이트해주는 식
            maxNum=graph[i][j]

def bfs(x,y,value,visited):
    q=deque()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    q.append((x,y))
    visited[x][y]=1
    
    while q:
        x,y= q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]>value and visited[nx][ny]==0:
                    # 쭉 방문하면서, 조건이 잠기지 않는 값들이기 때문에 최대 잠기는 수보다 높아야지만
                    # 마을의 개수를 셀 수 있음
                    visited[nx][ny]=1
                    q.append((nx,ny))

result=0
for i in range(maxNum): #예를 들어 6이면
    #0,1,2,3,4,5
    visited=[[0]*N for _ in range(N)]
    cnt=0
    
    for j in range(N):
        #0~4까지
        for k in range(N):
            #i=0일 때, (0,0), (0,1), (0,2), (0,3), (0,4)
            
            
            #만약 잠기지 않는 영역일 경우, 잠기지 않는 곳을 세어야 하기 때문에 함수를 적용시킨다
            if graph[j][k] > i and visited[j][k] ==0:
                #i보다 큰 경우, 잠기지 않는 것을 의미함
                bfs(j,k,i,visited)
                #함수에 넣음
                #함수를 다 돌고, cnt+=1을 하는거임
                
                cnt+=1
        
        if result<cnt:
            #cnt는 max을 나타냄(잠기지 않는 영역의 개수)
            #max값을 돌리면서, result값도 업데이트가 될텐데,
            #cnt값이 더 크면 result값을 해당값으로 업데이트
            #더이상 최댓값이 없다면 result는 고정해줌
            result=cnt

print(result)
                    
            
    

