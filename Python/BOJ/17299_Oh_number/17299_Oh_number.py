from collections import Counter
import sys
sys.stdin = open('input.txt')

# 크기가 N인 수열 A에서 오등큰수를 구하기
# 오등큰수 란 Ai가 수열에서 등장한 횟수를 F라고 했을시
# Ai의 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F보다 큰 수 중에서
# 가장 왼쪽에 있는 수를 의미함
# 오등큰수가 없으면 -1

# 예시
# A = [1, 1, 2, 3, 4, 2, 1]
# F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1 이다
# A1의 경우를 생각해볼때, 등장횟수가 3보다 큰 수는 없으므로 오등큰수 = -1
# NGF(3)의 경우, 등장횟수가 1보다 크며, 오른쪽에 있는 수가 있으므로 오등큰수 = 1
# NGF(4) = 2, NGF(5) = 2, NGF(6) = 1

N = int(input())
nums = list(map(int, input().split()))

num_count = Counter(nums)    # Counter 사용해서 요소별로 갯수 세기
result = [-1] * N
stack = [0]

# 현재 숫자가 스택 맨 위에 있는 값을 인덱스로 A에 있는 숫자보다 빈도수가 높으면
# result에 해당 숫자를 할당.
for i in range(1, N):
    while stack and num_count[nums[stack[-1]]] < num_count[nums[i]]:
        result[stack.pop()] = nums[i]

    stack.append(i)

print(*result)
