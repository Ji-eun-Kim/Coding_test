import sys
input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
    
# print(a)
# print(b)
# s = a[0]xb[0] + a[1]xb[1] + a[2]xb[2]

a.sort(reverse=True)
s = 0

for i in range(N):
    s+= min(a)*max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(s)
    
