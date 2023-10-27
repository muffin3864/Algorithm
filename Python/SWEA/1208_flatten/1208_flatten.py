import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    while dump != 0:
        boxes[boxes.index(min(boxes))] += 1
        boxes[boxes.index(max(boxes))] -= 1
        dump -= 1
        if max(boxes) - min(boxes) == 1:
            break

    result = max(boxes) - min(boxes)

    print(f'#{tc} {result}')
