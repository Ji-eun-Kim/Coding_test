# -*- coding: utf-8 -*-
"""[II] 음계 (2920번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dlE4KnIaPWeZCbXmHKCvfnWx7QAUrmk5
"""

a= list(map(int, input().split()))

if a== sorted(a):
  print('ascending')
elif a== sorted(a,reverse=True):
  print('descending')
else:
  print('mixed')