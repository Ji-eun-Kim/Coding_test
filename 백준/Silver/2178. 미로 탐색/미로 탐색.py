from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0,0)])

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < N and 0<=next_y < M:
            if graph[next_x][next_y] ==1:
                queue.append((next_x,next_y))
                graph[next_x][next_y] = graph[x][y] + 1 #이동한 칸 수 누적 

print(graph[N-1][M-1]) #인덱스는 0부터 시작