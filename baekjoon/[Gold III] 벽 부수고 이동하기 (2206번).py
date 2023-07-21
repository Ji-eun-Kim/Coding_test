#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

#벽 count해서 벽 뿌실 수 있는지 없는지 count
#만약 한번도 안뚫었다면 count+=1 하고, 그 칸에 이동 업데이트 +1

n,m=map(int,input().split())
graph=[]

visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1

for i in range(n):
    graph.append(list(map(int,input())))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y,z):
    queue=deque()
    queue.append((x,y,z))
    
    while queue:
        x,y,z=queue.popleft()
        
        if x==n-1 and y==m-1:
            return visited[x][y][z]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
                # 다음 이동할 곳이 벽이고, 벽 아직 안뿌셔본 경우
            if graph[nx][ny]==1 and z==0:
                visited[nx][ny][1]=visited[x][y][0] +1
                queue.append((nx,ny,1))
            
            # 다음 이동할 곳이 벽이 아니고, 방문하지 않은 경우, 앞으로 한칸 이동
            elif graph[nx][ny]==0 and visited[nx][ny][z]==0:
                visited[nx][ny][z]=visited[x][y][z]+1
                queue.append((nx,ny,z))
    return -1

print(bfs(0,0,0))


# In[2]:


[[[0] * 2 for _ in range(4)] for _ in range(6)]


# In[ ]:




