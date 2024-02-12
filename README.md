# 사람의 움직임 탐지 후 0~1 사이의 숫자로 표현
## 프로그램 소개
Mediapipe의 pose landmark 기술로 사람의 움직임을 1초마다 탐지함. 그 후 움직임의 정도를 0~1 사이의 값으로 정규화하여 출력함.

## 사용 환경
Python 3.10.11<Br>
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

## 파일 설명
### CamVER.py
컴퓨터의 내장 카메라를 통해 1초마다 움직임의 변화량 정도를 출력하는 코드

### VideoVER.py
"1sec-2mp4"라는 임의의 1초짜리 동영상을 0초, 1초마다 프레임을 캡쳐해 움직임의 변화량 정도를 출력하는 코드