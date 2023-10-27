# 최소 방의 개수 구하기, 여자 남자 따로
# K = 방에 들어가는 최대 인원 수
students, max_room = map(int, input().split())  # students = 학생 수, max_room = 방 인원 수

# 학년 별 인원 구하기
student_list = [[0,0,0,0,0,0],[0,0,0,0,0,0]]


for i in range(students):
    gender, year = map(int, input().split())  # S = 성별, Y = 학년
    # student_list 안에 성별, 학년 집어넣기
    student_list[gender][year-1] += 1

# 필요한 방의 갯수
need_room = 0

# student_list 안에서 학년별 숫자 들고 와서 방 인원수 비교해서 몇명 드가는지 체크
for gender_list in student_list:
    for year_numbers in gender_list:

        # 학년별 숫자 / 방 최대 인원수

        # 나머지 0이면 그냥 몫 더하기
        if year_numbers % max_room == 0:
            need_room += year_numbers // max_room
        # 나머지 0 아니면, 1 추가
        else:
            need_room += year_numbers // max_room + 1

print(need_room)




