N, M =map(int,input().split())

num_list = [i+1 for i in range(N)]
# print(num_list)

for _ in range(M):
    a, b = map(int,input().split())
    temp_list=[]
    for i in range(a-1,b,1):
        temp_list.append(num_list[i])
    k =0
    for j in range(a-1,b,1):
        num_list[j] = temp_list[b-a-k]
        k += 1

print(*num_list)
