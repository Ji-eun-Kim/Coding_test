# -*- coding: utf-8 -*-
"""[Silver V] 괄호 (9012번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WR5PVgQ9HTO9SBvclR8qCNh57ZaWumzs
"""

T=int(input())

for i in range(T):
  ps= list(input())
  sum=0

  for j in ps:
    if '(' in j:
      sum+=1
    elif ')' in j:
      sum-=1
    if sum<0: # ')'가 더 많은 경우
      print('NO')
      break #무한 - 방지를 위해
    
  if sum>0: #반복을 다 돌리고 난 후에도 0보다 크면
    print('NO')
  elif sum==0: 
    print('YES')