# -*- coding: utf-8 -*-
"""[Silver III]  통계학 (2108번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hu_01eziGLRA1DrArS7AoqZ1Dhvlc_4_
"""

from collections import Counter
import sys

def statistics(numbers):
  numbers.sort()

  cnt= Counter(numbers).most_common(2) 
  #빈도수가 가장 높은 숫자 2개가 출력
  #이 친구의 특징은 빈도수가 높은애들부터 출력
  #만약 빈도수가 같은 애들이 여러개면 sort한 수부터 출력( 오름차순 순으로로)

  #평균
  print(round(sum(numbers)/len(numbers)))
  #중앙값값
  print(numbers[len(numbers)//2])
  #최빈값
  if len(numbers)>1: 
    if cnt[0][1]==cnt[1][1]:
      print(cnt[1][0]) # 두번째로 작은 값이므로 -> 즉, 첫번째로 작은 값 다음이 두번째로 작은 값
    else:
      print(cnt[0][0]) #빈도 값이 다를 경우 앞에 있는 친구를 print
  else:
    print(cnt[0][0])

  #범위
  print(max(numbers)-min(numbers))


if __name__=='__main__':
  numbers=[]
  for _ in range(int(sys.stdin.readline())):
    num= int(sys.stdin.readline())
    numbers.append(num)

  statistics(numbers=numbers)