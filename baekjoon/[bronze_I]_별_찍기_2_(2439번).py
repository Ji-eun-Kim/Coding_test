# -*- coding: utf-8 -*-
"""[Bronze I] 별 찍기-2 (2439번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bpiL6F9Jb38Yfq5qxCYywTisI-ph7WY_
"""

N=int(input()) #5

for i in range(1, N+1):
  print(' '*(N-i)+ '*'*i)