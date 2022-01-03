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
	data := make([]Content, 2)

	data[0].Index = 1
	data[0].User.Name = "JS"
	data[0].User.Email = "js@cleancode.kr"
	data[0].Title = "hi golang"
	data[0].Content = "Hello"
	data[0].Connectors[0].Index = 1
	data[0].Connectors[0].User.Name = "JS2"
	data[0].Connectors[0].User.Email = "js2@cleancode.kr"
	data[0].Connectors[0].Content = "Hello2"

	doc, _ := json.Marshal(data)

	fmt.Println(string(doc))
}