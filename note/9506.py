def perfect(n):
    list_a = []
    for i in range(n-1):
        if n%(i+1) ==0 :
            list_a.append(i+1)
    if sum(list_a) ==n:
        divisors = " + ".join(map(str,list_a))
        print(f"{n} = {divisors}")
    else :
        print(f"{n} is NOT perfect.")
    

while True:
    n=int(input())
    if n == -1:
        break
    else:
        perfect(n)
