FROM python:3.8.5

# 이미지 생성 과정에서 실행할 명령어
RUN pip3 install pandas dash

# 이미지 내에서 명령어를 실행할(현 위치로 잡을) 디렉토리 설정
WORKDIR /

EXPOSE 8050

# 컨테이너 실행시 실행할 명령어
CMD ["python3", "./src/main.py"]

