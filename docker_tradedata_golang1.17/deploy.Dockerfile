#application compilation container
# FROM golang:1.14.1-alpine3.11 as builder
FROM golang:1.17-alpine3.15 as builder
WORKDIR /app
COPY . .

RUN apk update && \
    apk add git && \
    go get github.com/lib/pq \
    go build -o /go-app ./main.go

EXPOSE 5000

#executable container with compile files
FROM alpine:3.15
COPY --from=builder /go-app .
ENTRYPOINT ["./go-app"]