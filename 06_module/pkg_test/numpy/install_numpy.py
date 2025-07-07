### 문제 4: **pip로 패키지 설치 연습**

# 다람쥐는 `numpy` 라이브러리를 설치하여 업무 데이터를 처리하려고 합니다.

# 1. 터미널에서 `numpy`를 설치하세요.
    
#     ```bash
#     pip install numpy
#     ```
    
# 2. `numpy`의 mean() 함수를 사용해 배열의 평균을 계산하세요.

from numpy import mean

lst = [10, 8, 25, 7, 1]

print(mean(lst))