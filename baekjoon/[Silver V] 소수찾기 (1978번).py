# -*- coding: utf-8 -*-
"""[Silver V] 소수찾기 (1978번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MvUgRKDjHKRB51_Nvo7ssXnhqSBUn7Y7
"""

N= int(input())
numbers= map(int, input().split())
cnt=0

for m in numbers: #1 3 5 7 #8
  error=0
  if m>1:
    for j in range(2,m): # 2 3 4 5 6 7
      if m%j==0: #소수가 아님
        error+=1
    if error==0:
      cnt+=1
        
print(cnt)