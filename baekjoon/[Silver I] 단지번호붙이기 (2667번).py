#!/usr/bin/env python
# coding: utf-8

# In[9]:


from collections import deque

#왼오앞뒤
dx=[0,0,1,-1]
dy=[-1,1,0,0]


def bfs(graph,a,b):
    n=len(graph)
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0 #처음 시작할 때, 아무 좌표를 지나기 때문에, 지남처리로 해줌
    count=1 #지나갔다고 가정했기에 +1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            newx=x+dx[i]
            newy=y+dy[i]
            #왼오앞뒤 가보기
            if newx<0 or newx>=n or newy<0 or newy>=n:
                continue
            if graph[newx][newy]==1:
                graph[newx][newy]=0
                queue.append((newx,newy))
                #새로 움직인 좌표 중, 해당하면 +1
                count+=1 #마을 하나 안에 있는 집의 총 개수
    return count



n=int(input()) #n*n
graph=[]
for i in range(n): #7번만큼 반복
    graph.append(list(map(int,input()))) #바둑판 입력받는 곳

#함수를 통해 나온 값 count를 차례대로 저장시킴
cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            cnt.append(bfs(graph,i,j))
            
#정렬 및 출력
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])


# In[1]:


n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False
            
count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True: #7,7 다 돌아다님
            num.append(count) #7 8 9 
            result += 1 #3
            count = 0

num.sort() # 7 8 9
print(result)# 3
for i in range(len(num)): #3
    print(num[i])#7 8 9


# In[ ]:




