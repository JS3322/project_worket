FROM golang:1.17-alpine3.15
# FROM golang:alpine as builder

WORKDIR /app
COPY . .

RUN apk update && \
    apk add git

EXPOSE 5000

CMD ["reflex", "-c", "reflex.conf"]