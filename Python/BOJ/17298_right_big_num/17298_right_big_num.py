import sys
sys.stdin = open('input1.txt')

# 기준이 되는 숫자 오른쪽에 순차대로 비교해서 큰값이 존재한다면 리스트에 넣고
# 큰값이 존재하지 않으면 -1을 리스트에 넣기

N = int(input())
nums = list(map(int, input().split()))

right_nums = [-1] * N
stack = []
# 스택에 넣고 다음 원소로 이동해서 비교해서 큰수가 있으면 right_nums에 넣어준다.
for i in range(N):
    while stack and stack[-1][0] < nums[i]:
        tmp, idx = stack.pop()  # pop하면서 right_nums에 넣어주기
        right_nums[idx] = nums[i]   # 스택에 있는 인덱스 위치에 현재 i값의 숫자를 nums에 대입
    stack.append([nums[i], i])

print(*right_nums)