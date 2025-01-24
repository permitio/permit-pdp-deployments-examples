import pulumi
from pulumi_kubernetes.core.v1 import Namespace
from pulumi_kubernetes.helm.v3 import Release, ReleaseArgs, RepositoryOptsArgs

# Create namespace
pdp_namespace = Namespace("pdp-namespace", metadata={"name": "pdp"})

# Define Pulumi stack
config = pulumi.Config()

pdp_release = Release(
    "pdp",
    ReleaseArgs(
        chart="pdp",
        version="0.0.2",
        namespace=pdp_namespace.metadata["name"],
        repository_opts=RepositoryOptsArgs(
            repo="https://permitio.github.io/PDP"
        ),
        values={
            "pdp": {
                "ApiKey": config.require_secret("apiKey")
            }
        }
    )
)