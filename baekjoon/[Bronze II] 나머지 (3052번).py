# -*- coding: utf-8 -*-
"""[II]나머지(3052번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wmUt50p23k3XUPBAHSkm-f9ndGkagxuT
"""

lst= []
for i in range(10):
  A= int(input())
  lst.append(A)

lst2=[]

for i in lst:
  lst2.append(i%42)
print(len(set(lst2)))