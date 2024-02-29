# Helm install

1. clone the repo: https://github.com/permitio/sidecar
2. cd to charts/pdp

3. ```helm install pdp . --set pdp.ApiKey=<API_KEY> --create-namespace --namespace pdp --wait```