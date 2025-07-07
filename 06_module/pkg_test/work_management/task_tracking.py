#     - `task_tracking.py`: 작업 상태를 관리하는 모듈
        
#         ```
#         함수 start_task(task):"작업 '{task}' 시작됨." 반환
#         함수 end_task(task): "작업 '{task}' 종료됨." 반환
#         ```

def start_task(task):
    return f'작업 {task} 시작됨'

def end_task(task):
    return f'작업 {task}종료됨'