package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = "123456"
	dbname   = "postgres"
)

func main() {
	fmt.Println("START Connect")
	psqlconn := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)

	db, err := sql.Open("postgres", psqlconn)
	CheckError(err)
	defer db.Close()

	query := `insert into "table_test"("name") values("이름990")`
	insertDB(query, db)

}

func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}

func insertDB(query string, db *sql.DB) {

	insertStmt := query
	_, e := db.Exec(insertStmt)
	fmt.Println(e)
	// CheckError(e)
	defer db.Close()
}
