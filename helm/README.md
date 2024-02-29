# Helm install

1. helm repo add pdp https://permitio.github.io/sidecar

2. ```helm install pdp pdp/pdp --set pdp.ApiKey=<API_KEY> --create-namespace --namespace pdp --wait```