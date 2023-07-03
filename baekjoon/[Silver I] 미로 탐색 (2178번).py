#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque

N,M= map(int,input().split())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input())))

dirR= [-1,1,0,0]
dirC= [0,0,1,-1]
    
def bfs(x,y):
    queue= deque()
    queue.append((x,y)) #해당 x,y 값 위치 넣음
    
    while queue:
        x,y= queue.popleft()
        
        for i in range(4):
            nextx=x+dirR[i] #행
            nexty=y+dirC[i] #열
            
            if nextx<0 or nextx>=N or nexty<0 or nexty>=M:
                continue
                
            if graph[nextx][nexty]==0:
                continue
            
            if graph[nextx][nexty]==1:
                #해당 미로칸이 1인 경우에는, 그 자리에 1을 더해줘서 다음 위치의 값으로 업데이트해줌
                #그렇게 되면, 1을 몇 번 지나갔는지가 미로칸에 누적이 됨.
                graph[nextx][nexty]= graph[x][y]+1
                #queue 자리에 x,y 위치를 업데이트 해줌
                queue.append((nextx,nexty))
    #인덱스는 0부터 시작하므로
    return graph[N-1][M-1]
    
    
print(bfs(0,0))
                
        

