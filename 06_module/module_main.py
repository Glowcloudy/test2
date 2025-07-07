# import 구문 사용
# 1. our_class.py 모듈을 가져와서
import our_class
# 2. 선생님 이름과 학생 수를 출력하고
print(our_class.teacher_name)
print(our_class.student_count)
# 3. study() 함수와 lecture() 함수를 호출하고
our_class.study()
our_class.lecture()
# 4. 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
menu = ['떡볶이', '순대', '튀김', '마라탕', '초코프라푸치노']
# 5. go_lunch()함수를 호출해 오늘의 점심 메뉴를 출력해 보자!

print(our_class.go_lunch(menu))

