import sys
sys.stdin = open('input1.txt')

# 연속되는 온도 K개 만큼의 합 중 최대
# for문 안에 sum이 들어가면 시간 초과
# for문 안에서 sum 안쓰고 풀기
N, K = map(int, input().split())
temp = list(map(int, input().split()))

result = []
result.append(sum(temp[:K]))    # 1번째 값 담기

# 순회하면서 result에 더한값 담기
# 저장한 값에 이전값을 빼고 다음값을 더해 값을 추가해 나간다.
for i in range(N - K):
    result.append(result[i] - temp[i] + temp[K + i])
    #             이전 합      이전 값     다음 값

print(max(result))
