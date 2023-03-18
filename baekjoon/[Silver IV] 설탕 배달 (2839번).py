# -*- coding: utf-8 -*-
"""[Silver ] 설탕 배달 (2839번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PhQwbOP83KrZwyLkzXzVU6Cdnmot2VE6
"""

N= int(input())

#1) 5로 나눠지는 경우
if N%5==0:
  print(N//5) 
#2) 3과 5의 조합으로 하는 경우
else:
  cnt=0
  while N>0:
    N-=3
    cnt+=1
    if N%5==0: #3씩 빼주다가 5로 다 나눠지는 경우 ex) 17 => 14, 11, 8, 5 => 3x4 + 5x1 봉지
      cnt+=N//5
      print(cnt)
      break
    elif N==1 or N==2: # 3씩 빼주는데 1이거나 2가 남는 경우 -1로 반환 ex) 5 => 5-3 => 2이므로 -1 반환
      print(-1)
      break
    elif N==0:#3씩 계속 빼주는데 0이 될 경우 => 3의 배수를 뜻함
      print(cnt)
      break


#더 간단하게
N= int(input())

cnt=0

while N>=0:
  if N%5==0:
    cnt+=(N//5)
    print(cnt)
    break
  
  N-=3
  cnt+=1

else:
  print(-1)