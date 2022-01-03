FROM node:14-alpine as builder

#commands to be executed during image creation
# RUN npm install -g @nestjs/cli \
#     class-transformer class-validator \
#     @nestjs/mapped-types

#set the directory within the image to run commands (to take current location)
WORKDIR /home/node/app

COPY . /home/node/app

RUN npm install

#commands to be executed when the container is running
CMD ["npm", "run", "start"]

EXPOSE 3000

#executable container with compile files
FROM alpine:3.15
COPY --from=builder /go-app .
ENTRYPOINT ["./go-app"]