from collections import deque


def solution(n,computers):
    answer = 0
    visited = [0]*(n+1)

    def bfs(x):
        visited[x] = 1
        queue = deque()
        queue.append(x)
        while queue:
            x = queue.popleft()
            
            for i in range(n):
                if visited[i] == 0:
                    if computers[x][i] == 1:
                        visited[i] = 1
                        queue.append(i)


    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer+=1
    
    return answer