import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    c = int(input())
    coins.append(c) 

coins.reverse()


ans = 0

for coin in coins:
    if K >= coin:
        ans += K // coin #4200 // 1000 => 4
        K%=coin #200
        if K<=0:
            break

print(ans)      