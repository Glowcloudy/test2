# 1. `schedule_management`라는 패키지를 생성하고, 아래와 같은 모듈을 포함하세요:
#     - `calendar.py`: 다람쥐의 일정을 관리하는 모듈
        
#         ```
#         함수 add_event(event, date):"{date}에 '{event}' 일정이 추가되었습니다." 반환
#         함수 remove_event(event):"'{event}' 일정이 삭제되었습니다." 반환
#         ```

def add_event(event, date):
    return f'{date}에 {event} 일정이 추가되었습니다.'

def remove_event(evnet):
    return f'{evnet} 일정이 삭제되었습니다.'