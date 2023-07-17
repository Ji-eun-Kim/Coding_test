#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
import sys
input=sys.stdin.readline

N=int(input()) #7
visited=[False]*(N+1)
answer=[0]*(N+1)

graph=[[] for i in range(N+1)]
for i in range(N-1): #0~5 총 6번 반복
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,v,visited):
    queue=deque([v])
    visited[v]=True
    while queue:
        x=queue.popleft()
        for i in graph[x]: #4번 인덱스에 해당하는 리스트 값 하나하나를 의미함
            if not visited[i]:
                #7
                answer[i]=x
                #부모노드를 answer에 집어넣음
                #어차피 윗순서부터 for문이 돌아가기 때문에, 해당하는 값에 대한 부모노드가 ans에 들어감.
                queue.append(i)
                visited[i]=True

bfs(graph,1,visited)
for i in range(2,N+1):
    print(answer[i])

