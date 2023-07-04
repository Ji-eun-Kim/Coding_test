#!/usr/bin/env python
# coding: utf-8

# In[7]:


from collections import deque

n=int(input())
v=int(input())
graph = [[] for i in range(n+1)] #그래프 칸 만들기

visited=[0]*(n+1) #방문여부 칸 만들기

for i in range(v):
    a,b=map(int,input().split()) #인접 노드 입력칸
    graph[a]+=[b]
    graph[b]+=[a]
    
visited[1]=1

queue=deque([1])
while queue: # Q가 빌 때까지
    c= queue.popleft()
    for nx in graph[c]: #1번노드와 연결된 애들을 반복해서 돌릴거임
        if visited[nx]==0:
            queue.append(nx)
            visited[nx]=1

print(sum(visited)-1) #1번은 항상 1값이기에 
            
        


# In[8]:


n=int(input())
v=int(input())

graph = [[] for i in range(n+1)] #그래프 칸 만들기
visited=[0]*(n+1) #방문여부 칸 만들기

for i in range(v):
    a,b=map(int,input().split()) #인접 노드 입력칸
    graph[a]+=[b]
    graph[b]+=[a]
    
def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx] ==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)


# In[9]:


graph

