FROM golang:1.17-alpine3.15
# FROM golang:alpine as builder

WORKDIR /app
COPY . .

RUN apk update && \
    apk add git && \
    go get github.com/cespare/reflex && \
    go get github.com/lib/pq

EXPOSE 5000

CMD ["reflex", "-c", "reflex.conf"]