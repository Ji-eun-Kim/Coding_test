N = input().split('-') #-를 기준으로 1차 나눔
s=0
for i in N[0].split('+'): 
    #-를 기준으로 앞에 있는 값들은 다 더함
    s+=int(i)
for i in N[1:]:
    for j in i.split('+'): 
        #+를 기준으로 나눈 후, 뒤의 값을 다 빼줌
        #1번째 값부터는 다 빼주는 것으로 계산해주면 최솟값이 됨
        s-=int(j)
print(s)