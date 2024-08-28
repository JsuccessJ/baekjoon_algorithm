# 펠린드롬
word = input()
flag = True
for i in range(len(word)//2):
    if word[i]!=word[-i-1] :
        flag = False
        break
    
print(int(flag))
