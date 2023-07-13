#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import deque

n=5
k=17

def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            print(dist[x])
            break

        for nx in (x-1,x+1,2*x):
            if 0<=nx<=MAX and not dist[nx]:
                #방문을 안했다면
                #MAX 안의 값일 경우,
                dist[nx]=dist[x]+1 # 해당하는 곳에 시간 표시를 해줌
                #만약 x값이 0이었다면 1초가 되는 것임.
                q.append(nx)
                # 결국에는 4,6,10이 q에 저장
MAX=10**5
n,k = map(int,input().split())
dist=[0]*(MAX+1)

bfs()


# In[ ]:




