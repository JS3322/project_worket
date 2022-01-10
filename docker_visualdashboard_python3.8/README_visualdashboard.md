# 참조사이트
https://dash.plotly.com/dash-html-components
https://plotly.com/python/
https://dash.gallery/Portal/

- react python
Creating Your Own Components > React for Python Developers

# 이미지 생성 명령어 (현 파일과 같은 디렉토리에서)
docker build -t {이미지명} .
docker build -t gcr.io/homepage-336505/docker_visualdashboard_python3.8:1 .

# 컨테이너 생성 & 실행 명령어
docker run --name {컨테이너명} --volume $(pwd)/src:/src -p 8050:8050 {이미지명}
docker run --name vdb -v $(pwd)/src:/src -p 8050:8050 gcr.io/homepage-336505/docker_visualdashboard_python3.8:1
docker start vdb

# 배포
docker push gcr.io/homepage-336505/docker_visualdashboard_python3.8:2 (Docker file의 COPY Option Active)
docker run --name visualdashboard -p 8050:8050 gcr.io/homepage-336505/docker_visualdashboard_python3.8:2