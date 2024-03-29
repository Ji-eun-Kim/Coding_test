# -*- coding: utf-8 -*-
"""[Silver IV] 스택 (10828번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zf-8Mgu1VZhZC2rvLj7UTS0k8qPQVJte
"""

import sys
N=int(sys.stdin.readline().rstrip())

stack=[]

for i in range(N):
  word=sys.stdin.readline().rstrip().split()

  order=word[0]

  if order=='push':
    stack.append(word[1])
  
  elif order=='pop':
    if len(stack)==0:
      print(-1)
    else:
      print(stack.pop())
  
  elif order=='size':
    print(len(stack))
  
  elif order=='empty':
    if len(stack)==0:
      print(1)
    else:
      print(0)

  elif order=='top':
    if len(stack)==0:
      print(-1)
    else:
      print(stack[-1])