num_list=[int(input()) for i in range(10)]

rest_list=[num_list[i]%42 for i in range(10)]

count={}

for v in rest_list:
    if v in count:
        count[v] +=1
    else:
        count[v] =1
print(len(count))
