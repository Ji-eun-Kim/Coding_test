# -*- coding: utf-8 -*-
"""[Bronze III] 직각삼각형 (4153번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sd457ReQNn53Vm5ywEimARt6Qn8FkfAn
"""

while True:
  lst= list(map(int,input().split()))
  if lst[0]>0 and lst[1]>0 and lst[2]>0:
    c= max(lst)
    lst.remove(c)
    if c**2== lst[0]**2 + lst[1]**2:
      print('right')
    else:
      print('wrong')
  elif lst[0]==0 and lst[1]==0 and lst[2]==0:
    break