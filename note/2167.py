import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

arr = [list(map(int,inp().split())) for row in range(N)]

K = int(inp())

sum_list=[[0 for col in range(M+1)] for row in range(N+1)]
# print(sum_list)

for n in range(1,N+1,1):
    for m in range(1,M+1,1):
        sum_list[n][m] = arr[n-1][m-1] + sum_list[n][m-1] + sum_list[n-1][m] - sum_list[n-1][m-1]

            
for _ in range(K):
    i,j,x,y = map(int,inp().split())
    print(sum_list[x][y] - sum_list[x][j-1] - sum_list[i-1][y] + sum_list[i-1][j-1])


