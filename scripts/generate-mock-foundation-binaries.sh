GOOS=linux go build ./templates/hello-world.go
cp hello-world ./bin/controller
cp hello-world ./bin/proxyserver
cp hello-world ./bin/webhook
rm hello-world