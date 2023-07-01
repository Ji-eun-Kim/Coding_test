#!/usr/bin/env python
# coding: utf-8

# In[19]:


from collections import deque

N,M,V= map(int, input().split()) #4,5,1
#노드 개수, 간선 개수, 시작 노드

graph= [[False]*(N+1) for _ in range(N+1)] #  False list 생성

for _ in range(M): #5
    a,b= map(int, input().split())
    graph[a][b]= True
    graph[b][a]= True
    
visited1= [False] * (N+1) #dfs의 방문기록
visited2= [False] * (N+1) #bfs의 방문기록
#[False, False, False, False, False]

#거리는 짧은 애들부터, 같은 경우 작은 수부터
def bfs(V): #V=1
    q= deque([V])  #q= deque([1])
    visited2[V]= True #f,t,f,f,f
    while q:  #q가 빌 때까지 돈다.  #2가 될 때까지 -> 4가 될 때까지
        V= q.popleft() #큐에 있는 첫 번째 값을 꺼냄 1을 꺼냄 +  2 꺼냄
        print(V, end=" ") #1 ,+ 2
        for i in range(1,N+1): #i= 1,2,3,4
            if not visited2[i] and graph[V][i]:
                #visited2[1] and graph[1][1] -> true이므로 넘김
                #visited2[2] and graph[1][2] -> 해당됨
                #visited2[3] and graph[1][3] -> 해당됨
                
                #visited2[4] and graph[1][4] -> 해당됨
                
                
                q.append(i) # q= 2 +3 +4까지 추가함. (v가 1일 때) 
                visited2[i]=True # visited2[2]=True가 됨 + 3도 true 됨 + 4도
                
                

#깊이 우선 탐색 (노드 기준 짧은 애들부터)
def dfs(V): #1
    visited1[V]=True #2
    print(V, end =" ") #2
    for i in range(1, N+1): #1,2,3,4
        if not visited1[i] and graph[V][i]:
            # 만약 visited1에서 i 인덱스 위치를 방문하지 않았고,
            # V 노드와 연결이 되어있다면,
            dfs(i) # 2

dfs(V)
print()
bfs(V)  

