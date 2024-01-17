from collections import deque
#bfs ver 

N = int(input())
M = int(input()) #선 개수 

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

#graph
for i in range(M):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True


q = deque([1])
visited[1]=True

while q :
    cur = q.popleft()
    for next in range(1,N+1):
        if not visited[next] and graph[cur][next]:
            q.append(next)
            visited[next]=True

print(sum(visited)-1)

##############################################################################33

#dfs ver

N = int(input())
M = int(input()) #선 개수 

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)


#graph
for i in range(M):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True



def dfs(V):
    visited[V]=True
    for next in range(1,N+1): #1 ~ 7
        if not visited[next] and graph[V][next]:
            visited[next]=True
            dfs(next)


dfs(1)
print(sum(visited)-1)