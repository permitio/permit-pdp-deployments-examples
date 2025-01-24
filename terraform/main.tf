resource "helm_release" "pdp" {
  name       = "pdp"
  repository = "https://permitio.github.io/PDP"
  chart      = "pdp"
  version    = "0.0.2"
  namespace  = "pdp"  # Change the namespace if needed
  create_namespace = true # Change to false if the namespace already exists

  set {
    name  = "pdp.ApiKey"
    value = "<API_KEY>" # Insert the API key here
  }
}