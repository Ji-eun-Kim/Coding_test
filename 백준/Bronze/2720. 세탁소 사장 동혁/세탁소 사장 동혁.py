import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    c = int(input())
    for i in [25,10,5,1]:
        print(c//i, end = ' ')
        c = c%i