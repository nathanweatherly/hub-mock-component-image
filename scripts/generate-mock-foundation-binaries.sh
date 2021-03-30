GOOS=linux go build ./templates/hello-world.go
cp hello-world ./bin/controller
# cp hello-world ./bin/webhook
rm hello-world
GOOS=linux go build ./templates/mutating-webhook.go
mv mutating-webhook ./bin/webhook
cp ./templates/template-proxyserver-binary ./bin/proxyserver