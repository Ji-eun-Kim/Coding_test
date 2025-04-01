from collections import deque

def solution(maps):
    n,m = len(maps), len(maps[0]) #행, 열
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    maps[nx][ny] = maps[x][y]+1

    
    if maps[n-1][m-1] == 1: #벽이 막혀있다면 목표 지점 업데이트가 안되기 때문에 1일 수 밖에 없음
        return -1
    else:
        return maps[n-1][m-1]
