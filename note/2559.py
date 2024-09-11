N, K = map(int, input().split())

num_list = list(map(int,input().split()))

sum_k = [0]
for i in range(K):
    sum_k[0] += num_list[i]

for i in range(1,N-K+1,1):
    sum_k.append(sum_k[i-1] - num_list[i-1] + num_list[i-1+K])

print(max(sum_k))
