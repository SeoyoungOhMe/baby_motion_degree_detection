# 사람의 움직임 탐지 후 0~1 사이의 숫자로 표현
## 프로그램 소개
사람의 움직임을 mediapipe의 pose landmark 기술로 탐지함. 그 후 움직임의 정도를 0~1 사이의 값으로 정규화하여 출력함.

## 사용 환경 
Python 3.10.11
opencv-python, mediapipe, numpy 모듈 필요
```
pip install opencv-python mediapipe numpy
```

## 사용 방법
```
git clone https://github.com/SeoyoungOhMe/baby_motion_degree_detection.git

python CamVER.py
python VideoVER.py
```