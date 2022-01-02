FROM node:14-alpine

#commands to be executed during image creation
# RUN npm install -g @nestjs/cli \
#     class-transformer class-validator \
#     @nestjs/mapped-types

#set the directory within the image to run commands (to take current location)
WORKDIR /home/node/app

COPY package.json /home/node/app

RUN npm install

COPY . /home/node/app

#commands to be executed when the container is running
CMD ["npm", "run", "start"]

EXPOSE 3000
