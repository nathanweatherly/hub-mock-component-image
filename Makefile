gen-mock-charts:
	python3 ./scripts/generate-mock-charts.py

gen-helm-repo-index:
	python3 ./scripts/generate-helm-index.py

gen-mock-chart-repo: gen-mock-charts gen-helm-repo-index

del-mock-chart-repo:
	python3 ./scripts/delete-mock-charts-repo.py