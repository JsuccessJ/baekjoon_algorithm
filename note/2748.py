n = int(input())

fibo=[0,1]

for i in range(0,n-1,1):
    fibo.append(fibo[i+1]+fibo[i])

print(fibo[n])
