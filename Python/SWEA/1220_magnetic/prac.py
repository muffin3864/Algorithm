import sys
sys.stdin = open('input.txt')

# 위에서 n극, 아래에 s극 만나면 교착
# 만나지 않는 경우 테이블 밖으로 나감
# 교착 상태인 갯수 카운트

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    # 1.열에서 스택을 받아 1,2가 만나면 카운트
    for i in range(100):
        stack = []
        for j in range(100):
            if arr[j][i] == 1:
                stack.append(arr[j][i])
            elif stack and arr[j][i] == 2 and stack[-1] == 1:
                cnt += 1
                stack.clear()


    print(f'#{tc} {cnt}')