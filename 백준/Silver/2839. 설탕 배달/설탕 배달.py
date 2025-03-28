import sys
input = sys.stdin.readline

N = int(input())

bag = 0

# 18 // 5 => 3
# 18 % 5 => 3 // 3 => 1

# 1. 5로 나눠지는 경우
# 2. 5와 3으로 나눠지는 경우
# 3. 3으로 나눠지는 경우
# 4. 둘 의 조합으로 안되는 경우


while N >=0:
    if N % 5  == 0:
        bag += (N//5)
        print(bag)
        break
    N-=3
    bag+=1
else:
    print(-1)