package main

import (
	"fmt"
	"net/http"
	"time"
)

func Ping(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

func main() {

	http.HandleFunc("/healthz", Ping)
	http.HandleFunc("/readyz", Ping)
	http.ListenAndServe(":8000", nil)
	// http.ListenAndServe(":6443", nil) // This doesn't work; proxy server has HTTPS
	// err := http.ListenAndServeTLS(":6443", "", "", nil)
	// if err != nil {
	// 	log.Fatal("ListenAndServeTLS: ", err)
	// }
	for {
		time.Sleep(5 * time.Second)
		fmt.Println("Still Running...")
	}
}
