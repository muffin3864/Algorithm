import sys
sys.stdin = open('input.txt')

# 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점
# 4째 자리까지 반올림해서 함께 출력

total = 0
dic = dict()
while 1:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    total += 1   
    if word in dic:   # 전에 이미 나왔으면
        dic[word] += 1
    else:
        dic[word] = 1
sdic = dict(sorted(dic.items()))
for i in sdic:
    a = sdic[i]
    per = (a / total * 100)
    
    print("%s %.4f" %(i, per))
