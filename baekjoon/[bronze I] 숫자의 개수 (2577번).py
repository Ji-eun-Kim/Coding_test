# -*- coding: utf-8 -*-
"""[Bronze I] 숫자의 개수 (2577번)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z2uWcmvXqBGtUD09vZRQEK8oKhK7Cbl0
"""

A= int(input())
B= int(input())
C= int(input())

result= list(str(A*B*C));result

for i in range(10):#0 1 2 3 4 5 6 7
  print(result.count(str(i)))