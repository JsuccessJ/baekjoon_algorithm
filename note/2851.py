num_list=[]
sum_list=[]

for i in range(10):
    n = int(input())
    num_list.append(n)

sumN = 0

for num in num_list :
    sumN += num
    sum_list.append(sumN)

# print(sum_list)

for i in range(0,9,1):
    if sum_list[i] == 100 or sum_list[i+1] == 100:
        print(100)
        break
    elif sum_list[i]<100 and sum_list[i+1]>100 :
        if (100-sum_list[i]) < (sum_list[i+1]-100):
            print(sum_list[i])
            break
        else:
            print(sum_list[i+1])
            break
else:
    print(sum_list[-1]) # 모든 수의 합이 100이 안넘을때의 예외 조심
