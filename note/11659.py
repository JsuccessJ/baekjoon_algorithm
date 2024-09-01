import sys
input = sys.stdin.readline # 이 줄을 넣어주면 input()을 할 때 시간초과가 발생하지 않는다.

N, M = map(int,input().split())

numbers=list(map(int,input().split()))
sum_numbers=[0] # 0번 인덱스의 0을 미리넣어주는 좋은 방법
sum = 0
for i in numbers:
    sum += i
    sum_numbers.append(sum)

for _ in range(M):
    i,j = map(int,input().split())
    print(sum_numbers[j]-sum_numbers[i-1])
