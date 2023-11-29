import sys
sys.stdin = open('input1.txt')

# 처음에 replace를 그냥 썻는데 시간초과가 계속 뜸
# 스택으로 풀기
# 스택을 쌓다가 폭발 단어를 발견하면 폭발 단어만 pop하자

text = sys.stdin.readline().rstrip()
explosion_str = sys.stdin.readline().rstrip()

stack = []
explosion_len = len(explosion_str)

for i in range(len(text)):
    stack.append(text[i])

    # 스택에 폭발 단어 발견시
    if ''.join(stack[-explosion_len:]) == explosion_str:

        for _ in range(explosion_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
