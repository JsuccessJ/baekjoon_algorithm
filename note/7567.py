T = [i for i in str(input())]
def render(n, result = 0):
    if n == 0: # 맨 밑에 접시의 크기는 10
        return result + 10
    elif T[n] == T[n - 1]: # 포개진 경우
        result += 5
        return render(n - 1, result)
    else:
        result += 10 # 포개지지 않은 경우
        return render(n - 1, result)
print(render(len(T) - 1))
