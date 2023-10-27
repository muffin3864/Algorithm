import sys
sys.stdin = open('input.txt')

# 두번째 값을 첫번째 값보다 작은 것으로 임의로 선택
N = int(input())
num_count = []
# 앞에 값들로 뺄때 마다 스택에 쌓자
for i in range(1, N+1):
    numbers = []
    numbers.append(N)
    numbers.append(i)
    while True:
        num = numbers[-2] - numbers[-1]

        if numbers[-2] - numbers[-1] < 0:
            break

        numbers.append(num)

    num_count.append([len(numbers), numbers])

max_num = max(num_count)

print(max_num[0])
print(*max_num[1])