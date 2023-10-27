dwarf = []
for i in range(9):
    a =int(input())
    dwarf.append(a)

# 드워프 키 합
sum_dwarf = 0
for dwarf_stat in dwarf:
    sum_dwarf += dwarf_stat

# 키 합에서 2개를 뺐을때 100이 되는 요소 찾기

for i in range(9):
    for j in range(i+1, 9):
        if sum_dwarf - dwarf[i] - dwarf[j] == 100:
            wrong_dwarf_1 = dwarf[i]
            wrong_dwarf_2 = dwarf[j]

# 드워프 리스트에서 찾은 드워프 빼주기
dwarf.remove(wrong_dwarf_1)
dwarf.remove(wrong_dwarf_2)

# 드워프 오름차순 정렬
dwarf.sort()

print(*dwarf)