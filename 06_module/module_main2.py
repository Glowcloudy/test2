# import 구문 사용
# 1. our_class.py 모듈을 가져와서
from our_class import student_count, teacher_name, study, lecture, go_lunch
# 2. 선생님 이름과 학생 수를 출력하고
print(teacher_name)
print(student_count)
# 3. study() 함수와 lecture() 함수를 호출하고
study()
lecture()
# 4. 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menu = ['떡볶이', '순대', '튀김', '마라탕', '초코프라푸치노']
# 5. go_lunch()함수를 호출해 오늘의 점심 메뉴를 출력해 보자!

print(go_lunch(menu))