import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


#dfs (1,0) 이 처음으로 들어감
#dfs (2,1)
def dfs(start,depth):
    # 방문 표시
    visited[start]=True #1번째 방문처리
    for i in graph[start]: #graph[1] = 2,5 이므로 i=2,5가 됨
        #graph[2] = 1,5 이므로 i=1,5가 됨
        #visited[1]은 방문했으므로 아래 for문으로
        if not visited[i]: #만약 vistied[2],visited[5]를 방문하지 않았으면 반복
            # dfs(2), depth=1
            dfs(i, depth +1)
            
#입력값 정의
N, M = map(int, input().split())
graph=[[] for _ in range(N+1)] #7개
#[[], [], [], [], [], [], []]


for _ in range(M): #5 번 반복
    a,b= map(int,input().split())
    graph[a].append(b) 
    graph[b].append(a)
    #그래프 채우기
    
    
visited=[False]*(N+1) #1번인덱스부터 시작이므로
count=0


# i = 1 ~ 7 까지 반복
for i in range(1,N+1):
    #방문한 경우 계속 for 문 돌림
    # visited[3]은 방문하지 않았음
    if not visited[i]: #i =3
        if not graph[i]: #해당 정점이 연결된 그래프가 없다면
            count+=1 #개수를 +1
            visited[i]=True # 방문처리 visited[3]=True로 처리
        else: #연결된 그래프가 존재할 경우
            dfs(i,0)  # 탐색후, 개수 +1
            count+=1
print(count)