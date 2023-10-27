w, l = map(int, input().split())
cut = int(input())  # 자르는 횟수
# 잘라질 길이 리스트 만들기
width = [0, w]
length = [0, l]

for tc in range(cut):
    m, num = map(int, input().split())  # m=0,가로 m=1,세로  num = 점선 번호

    if m == 0:
        length.append(num)
    if m == 1:
        width.append(num)

width.sort()    # [0, 4, 10]
length.sort()   # [0, 2, 3, 8]

x_list = []
y_list = []

for i in range(len(width)-1):
    for j in range(len(length)-1):
        x = width[i+1] - width[i]
        y = length[j+1] - length[j]
        x_list.append(x)
        y_list.append(y)
        area = max(x_list) * max(y_list)

print(area)