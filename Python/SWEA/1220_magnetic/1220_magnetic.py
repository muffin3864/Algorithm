import sys
sys.stdin = open('input.txt')

# 모든 자성체들이 위, 아래로 1칸씩 이동(1은 아래로, 2는 위로 이동)
# 만나면 그자리에서 정지
# 만날게 없으면 테이블 밖으로 나감
# N,S 가 세트로 있어야 1개로 체크

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    count = 0
    # 1.열끼리 비교를 해야함
    for i in range(N):
        r, c = 0, i
        stack = []
        # 2. 숫자가 짝으로 있는지 비교하고 카운트(무조건 1이 위,2가 아래 여야함)
        while r < N:
            if not stack and arr[r][c] == 1:  # 스택이 비어있는 상태이면서 1 이면 stack에 넣음
                stack.append(1)
            elif stack and arr[r][c] == 2:  # 스택에 1이 있는 상태에서 2가 나오면 pop 해서 cnt에 더해주기
                count += stack.pop()
            r += 1

    print(f'#{tc} {count}')

