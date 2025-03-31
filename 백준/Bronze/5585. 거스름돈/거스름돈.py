n = int(input()) 
money = 1000-n
cnt = 0
for i in [500,100,50,10,5,1]:
    cnt += money//i
    money = money%i
    
print(cnt)