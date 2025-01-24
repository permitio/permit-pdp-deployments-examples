# Helm install

1. ```helm repo add pdp https://permitio.github.io/PDP```

2. ```helm install pdp pdp/pdp --set pdp.ApiKey=<API_KEY> --create-namespace --namespace pdp --wait```