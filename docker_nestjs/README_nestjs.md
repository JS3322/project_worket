# 이미지 생성 명령어 (현 파일과 같은 디렉토리에서)
docker build -t {이미지명} .
docker build -t github.io/js3322/docker_nestjs:1 .

# 컨테이너 생성 & 실행 명령어
docker run --name {컨테이너명} --volume $(pwd)/src:/src -p 3000:3000 {이미지명}
docker run --name nestjs -v $(pwd)/src:/src -p 3000:3000 github.io/js3322/docker_nestjs:1