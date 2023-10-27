import sys
sys.stdin = open('input.txt')

# 과제를 제출x 사람 번호를 오름차순 출력

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    K_num = list(map(int, input().split()))

    # 출석부 만들기 (오름차순으로 만들어짐)
    students = [i for i in range(1, N + 1)]

    # 출석부 - 과제 제출한 사람
    for i in K_num:
        students.remove(i)

    print(f'#{tc}', *students)