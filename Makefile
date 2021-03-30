check-env-vars:
	python3 ./scripts/check_env_vars.py

gen-mock-charts:
	python3 ./scripts/generate-mock-charts.py

gen-helm-repo-index:
	python3 ./scripts/generate-helm-index.py

gen-foundation-binaries:
	bash ./scripts/generate-mock-foundation-binaries.sh

gen-and-push-image:
	python3 ./scripts/generate-mock-images.py

gen-mock-image-manifest:
	python3 ./scripts/generate-mock-image-manifest.py

del-mock-chart-repo:
	rm -rf multiclusterhub

del-mock-image-manifests:
	rm -rf results

del-mock-bins:
	rm -rf bin/*

clean-up: 
	make del-mock-chart-repo 
	make del-mock-image-manifests 
	make del-mock-bins

build: 
	make check-env-vars
	make clean-up 
	make gen-mock-charts 
	make gen-helm-repo-index 
	make gen-foundation-binaries
	make gen-and-push-image
	make gen-mock-image-manifest