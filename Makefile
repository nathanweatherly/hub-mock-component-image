gen-and-push-all-images:
	python3 ./scripts/generate-mock-images.py

gen-mock-charts:
	python3 ./scripts/generate-mock-charts.py

gen-helm-repo-index:
	python3 ./scripts/generate-helm-index.py

gen-mock-chart-repo: gen-mock-charts gen-helm-repo-index

del-mock-chart-repo:
	rm -rf multiclusterhub

gen-mock-image-manifest:
	python3 ./scripts/generate-mock-image-manifest.py

del-mock-image-manifests:
	rm -rf results

build-foundation-binaries:
	bash ./scripts/generate-mock-foundation-binaries.sh