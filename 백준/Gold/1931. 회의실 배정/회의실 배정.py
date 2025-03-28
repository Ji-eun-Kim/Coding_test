import sys
input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    start, end = map(int, input().split())
    lst.append((start,end))

lst.sort(key = lambda x: (x[1],x[0]))

cnt = 1
end = lst[0][1] # 4
for i in range(1,N):
    if lst[i][0]>=end: # 5>4
        cnt+=1
        end = lst[i][1]

print(cnt)