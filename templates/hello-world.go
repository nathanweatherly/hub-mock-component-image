package main

import (
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io/ioutil"
	v1 "k8s.io/kubernetes/staging/src/k8s.io/api/admission/v1"
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

func webhookRun() error {
	http.HandleFunc("/mutating", webhookServer)

	server := &http.Server{
		Addr:      ":8000",
		TLSConfig: configTLS(),
	}
	err := server.ListenAndServeTLS("", "")
	if err != nil {
		fmt.Errorf("Listen server tls error: %+v", err)
		return err
	}

	return nil
}

func webhookServer(w http.ResponseWriter, r *http.Request){
	var body []byte
	if r.Body != nil {
		if data, err := ioutil.ReadAll(r.Body); err == nil {
			body = data
		}
	}

	// The AdmissionReview that was sent to the webhook
	requestedAdmissionReview := v1.AdmissionReview{}

	// The AdmissionReview that will be returned
	responseAdmissionReview := v1.AdmissionReview{
		Response: &v1.AdmissionResponse{Allowed: true},
	}

	if err := json.Unmarshal(body, &requestedAdmissionReview); err != nil {
		fmt.Errorf("error %v",err)
		return
	}

	responseAdmissionReview.Kind = requestedAdmissionReview.Kind
	responseAdmissionReview.APIVersion = requestedAdmissionReview.APIVersion
	// Return the same UID
	responseAdmissionReview.Response.UID = requestedAdmissionReview.Request.UID

	respBytes, err := json.Marshal(responseAdmissionReview)
	if err != nil {
		fmt.Errorf("error %v",err)
		return
	}
	if _, err := w.Write(respBytes); err != nil {
		fmt.Errorf("error %v",err)
		return
	}
}

func configTLS() *tls.Config {
	certFile := "/var/run/ocm-webhook/tls.crt"
	keyFile := "/var/run/ocm-webhook/tls.key"
	sCert, err := tls.LoadX509KeyPair(certFile, keyFile)
	if err != nil {
		fmt.Errorf("error %v",err)
	}

	return &tls.Config{
		MinVersion:   tls.VersionTLS12,
		Certificates: []tls.Certificate{sCert},
	}
}
