N, M =map(int,input().split())

num_list = [i+1 for i in range(N)]
# print(num_list)

for _ in range(M):
    a, b = map(int,input().split())
    temp = num_list[a-1]
    num_list[a-1] = num_list[b-1]
    num_list[b-1] = temp

print(*num_list)
