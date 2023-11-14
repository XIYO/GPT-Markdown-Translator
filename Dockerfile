# 베이스 이미지를 지정합니다. 여기서는 Python 3을 사용합니다.
FROM python:3

# 애플리케이션 파일을 컨테이너의 /app 디렉토리로 복사합니다.
WORKDIR /app
COPY . /app

# 필요한 Python 패키지를 설치합니다.
RUN pip install -r requirements.txt

# 컨테이너가 시작될 때 실행될 명령을 지정합니다.
CMD ["python", "./app.py"]
