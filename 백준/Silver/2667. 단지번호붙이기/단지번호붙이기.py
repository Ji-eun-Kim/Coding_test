#dfs
N= int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(graph,x,y):
    n = len(graph)
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y]==1:
        global count
        count+=1
        graph[x][y]=0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph,nx,ny)
        return True
    return False

count = 0
result=0
num=[]

for i in range(N):
    for j in range(N):
        if dfs(graph,i, j) == True:
            num.append(count) 
            count = 0

num.sort()
print(len(num))
for i in num:
    print(i)