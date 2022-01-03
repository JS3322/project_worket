package main

import (
	"encoding/json"
	"fmt"
)

type User struct {
	Name string `json:"name"`
	Email string `json:"email"`
}

type Connector struct {
	Index uint64 `json:"index"`
	User User `json:"user"`
	Content string `json:"content"`
}

type Content struct {
	Index uint64 `json:"index"`
	User User `json:"user"`
	Title string `json:"title"`
	Content string `json:"content"`
	Connectors []Connector `json:"connector"`
}

func main() {
	doc := `
	[{
		"index": 1,
		"user": {
			"name": "js",
			"email": "js@cleancode.kr"
		},
		"title": "Hello, world!",
		"content": "Hello~",
		"connector": [{
			"index": 1,
			"user": {
				"name": "js2",
				"email": "js2@cleancode.kr"
			},
			"content": "Hello js"
		}]
	}]
	`

	var data []Content 

	json.Unmarshal([]byte(doc), &data) 

	fmt.Println(data) 
}