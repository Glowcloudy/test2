import random

teacher_name = '다람쥐'
student_count = 29
# study()
# student_count 명의 학생들이 열심히 공부를 한다!!! 출력
def study():
    return print(f'{student_count}명의 학생들이 열심히 공부를 한다!!!')

# lecture()
# teacher_name 선생님이 수업 중이다~~~~~ 출력
def lecture():
    return print(f'{teacher_name} 선생님이 수업 중이다~~~~~')


# go_lunch()
# 파라미터 -> menus 리스트
# random 모듈의 choice 함수를 이용 -> 하나 선택
# return ????
def go_lunch(menus):
    return random.choice(menus)

