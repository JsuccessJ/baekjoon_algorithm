N = int(input())

num_list = list(map(int,input().split()))
sort_list = sorted(num_list)

count = 0

for k in range(N):
    i = 0
    j = N-1
    while i<j :
        if sort_list[i]+sort_list[j] ==sort_list[k]:
            if i!=k and j!=k :
                count += 1
                break
            elif i == k :
                i += 1
            elif j == k :
                j -= 1
        elif sort_list[i]+sort_list[j] > sort_list[k]:
            j -= 1
        else:
            i += 1
                
print(count)
