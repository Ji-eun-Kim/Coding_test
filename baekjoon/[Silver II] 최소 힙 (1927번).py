from sys import stdin
input=stdin.readline

import heapq

n=int(input())
heap=[]
for i in range(n):
    x=int(input())
    if x==0:
        if heap: #heap이 비어있지 않은 경우
            print(heap[0]) #가장 최솟값을 출력
            heapq.heappop(heap) #그 값을 삭제
        else:
            print(0) #비었다면 0을 출력
    else:
        heapq.heappush(heap,x) #아닌 경우, heap에 추가 후 정렬 