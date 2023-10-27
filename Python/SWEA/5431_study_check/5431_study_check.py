import sys
sys.stdin = open('input.txt')

# N = 수강생의 수
# K = 과제를 제출한 사람의 수
# [] = 과제 제출한 사람의 번호

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    study = list(map(int, input().split()))

    students = []
    for i in range(1, N + 1):
        students.append(i)
    # [1, 2, 3, 4, 5]
    for i in range(K):
        students.remove(study[i])

    print(f'#{tc}', *students)