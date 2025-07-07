### 문제 2: **다람쥐의 업무 관리 패키지**

# 다람쥐는 팀의 업무를 관리하기 위한 패키지를 작성하려고 합니다.

# 1. `work_management`라는 패키지를 생성하고, 아래와 같은 모듈을 포함하세요:
#     - `task_tracking.py`: 작업 상태를 관리하는 모듈
        
#         ```
#         함수 start_task(task):"작업 '{task}' 시작됨." 반환
#         함수 end_task(task): "작업 '{task}' 종료됨." 반환
#         ```
        
#     - `reporting.py`: 업무 보고를 관리하는 모듈
        
#         ```
#         함수 generate_report(task): "'{task}' 작업 보고서 생성됨." 반환
#         ```
        
# 2. 메인 스크립트에서 이 패키지를 불러와 아래와 같이 출력하세요:
from task_tracking import start_task, end_task
from reporting import generate_report

print(start_task("코드 리뷰"))
print(end_task("코드 리뷰"))
print(generate_report('코드리뷰'))