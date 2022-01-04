FROM python

# 이미지 생성 과정에서 실행할 명령어
RUN pip install pandas dash=1.14.0 jupyterlab

# 이미지 내에서 명령어를 실행할(현 위치로 잡을) 디렉토리 설정
WORKDIR /usr/src/app

# 컨테이너 실행시 실행할 명령어
CMD ["python3", "backend.py"]

# 이미지 생성 명령어 (현 파일과 같은 디렉토리에서)
# docker build -t {이미지명} .

# 컨테이너 생성 & 실행 명령어
# docker run --name {컨테이너명} -v $(pwd):/usr/src/app -p 8888:8888 -p 8050:8050 {이미지명}

