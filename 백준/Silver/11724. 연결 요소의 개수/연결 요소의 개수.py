from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0]*(N+1)

def bfs(graph,q,visited):
    queue = deque()
    queue.append(q)
    visited[q] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
            
cnt=0            
for i in range(1,N+1):
    if visited[i]==0:
        bfs(graph,i,visited)
        cnt+=1        
        
print(cnt)                