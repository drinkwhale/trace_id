# 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스 복사
COPY app.py .

# 컨테이너 포트 오픈
EXPOSE 8080

# 앱 실행
CMD ["python", "app.py"]