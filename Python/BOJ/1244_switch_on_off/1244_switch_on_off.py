import sys
sys.stdin = open('input.txt')

# 스위치 켜고, 끄기
def turn(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split())) # 스위치 계산에 사용 안되는 -1을 추가해 리스트의 대칭을 맞춰줌
# [0, 1, 0, 1, 0, 0, 0, 1]
student_number = int(input())

for _ in range(student_number):
    gender, num = map(int, input().split())

    # 남자일때 (3, 6번 스위치 변경)
    if gender == 1:
        for i in range(num, N+1, num):
            turn(i)
    # [0, 1, 1, 1, 0, 1, 0, 1]

    # 여자일때 (1, 2, 3, 4, 5번 스위치 변경)
    else:
        turn(num)
        for j in range(N // 2): # 0,1,2,3
            if num + j > N or num - j < 1:
                break
            if switch[num + j] == switch[num - j]:
                turn(num + j)
                turn(num - j)
            else:
                break
    # [1, 0, 0, 0, 1, 1, 0, 1]

for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()