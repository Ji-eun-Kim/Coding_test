#!/usr/bin/env python
# coding: utf-8

# In[8]:


n=int(input())
count=0
stack=[]
ans=[]
find=True

now=1

for i in range(n):
    num=int(input())
    while now<=num:
        stack.append(now)
        ans.append('+')
        now+=1
    if stack[-1]==num:
        stack.pop()
        ans.append('-')
    else:
        find=False
        
if not find:
    print('NO')
else:
    for i in ans:
        print(i)
    
        



# In[ ]:




