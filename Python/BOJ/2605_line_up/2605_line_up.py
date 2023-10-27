# 2605_줄세우기

# 1명 추가 될때 마다 리스트에 추가
# 리스트에 추가될때 뽑은 번호에 따라 순서 지정해서 추가됨

students = int(input())
number = list(map(int, input().split()))  # 번호 뽑기
# 0 1 1 3 2

line_up = []
for i in range(students):  # 학생 1명씩 줄서기
    # 위치 역으로 뒤집으면서 리스트에 넣기
    line_up.insert(i - number[i], i + 1)
    # 위치값이 0이고 이미 0번째 요소가 있으면 그 뒤로 들어간다
    print(line_up)

for j in line_up:
    print(j, end = ' ')
    # 4 2 5 3 1





















