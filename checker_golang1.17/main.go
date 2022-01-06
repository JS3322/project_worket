package main

import (
	"errors"
	"fmt"
	"net/http"
)

type requestResult struct {
	url    string
	status string
}

var errRequestFailed = errors.New("Request failed")

func main() {
	API_KEY := "testcode"
	urls := []string{
		"https://www.cleancode.shop/",
		"https://www.cleancode.kr/",
		"http://web.cleancode.kr/",
		"http://code.cleancode.kr/",
		"https://web.cleancode.kr/",
		"http://api.ganada.kr/",
		"http://www.ganada.kr/",
		"http://code.ganada.kr/",
		"http://code.web.cleancode.kr/",
		"https://www.google.com/",
		"https://www.naver.com/",
		"https://www.instagram.com/",
		"https://api.themoviedb.org/3/movie/popular?api_key="+API_KEY,
	}
	results := make(map[string]string)
	c := make(chan requestResult)

	for _, url := range urls {
		go hitURL(url, c)
	}

	for i := 0; i < len(urls); i++ {
		result := <-c
		results[result.url] = result.status
	}

	for url, status := range results {
		fmt.Println(url, status)
	}
}

func hitURL(url string, c chan<- requestResult) {
	fmt.Println("Checking:", url)
	resp, err := http.Get(url)
	status := "OK"
	if err != nil || resp.StatusCode >= 400 {
		status = "FAILED"
	}
	c <- requestResult{url: url, status: status}
}