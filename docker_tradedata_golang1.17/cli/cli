package cli

import (
	"flag"
	"fmt"
	"os"

	"github.com/JS3322/project_worket/docker_tradedata_golang1.17/explorer"
	"github.com/JS3322/project_worket/docker_tradedata_golang1.17/rest"
)

func usage() {
	fmt.Printf("TEST to Cleancode\n\n")
	fmt.Printf("Please use the following flags:\n\n")
	fmt.Printf("-port:		Set the PORT of the server\n")
	fmt.Printf("-mode:		Select mode'\n\n")
	os.Exit(0)
}

func Start() {
	if len(os.Args) == 1 {
		usage()
	}

	port := flag.Int("port", 4000, "Set port of the server")
	mode := flag.String("mode", "api", "Choose between 'view' and 'api'")

	flag.Parse()

	switch *mode {
	case "api":
		rest.Start(*port)
	case "view":
		explorer.Start(*port)
	default:
		usage()
	}
}
