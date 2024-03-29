# Deploying PDP on GCP Cloud Run
Our PDP image runs on GCP Cloud Run without any modification. You can deploy it by using our public image on [Docker Hub](https://hub.docker.com/r/oryd/pdp).

## Step by step guide
In the following step, we will show you how to deploy our PDP image on GCP Cloud Run,
And in the end we'll share the final YAML file that you can use to deploy the PDP on GCP Cloud Run.

### 1. Create a new Cloud Run service
Create a new Cloud Run service by clicking on the `Create Service` button in the Cloud Run dashboard.

![Create Service](../images/gcp/1.png)

### 2. Configure the service
Now, we'll set the name, image and some other configurations for the service.
First, in the "Container Image URL" field, enter the following image `permitio/pdp-v2:latest`.
Then, set the name of the service to the name that fits you.

![Configure Service](../images/gcp/2.png)

Obviously, you can change the region and other configurations as you wish.

### 3. Adjust the Auto Scaling configuration (Recommended)
In the "Auto Scaling" section, set the "Minimum number of instances" to 1.
This will make sure that there is always at least one instance of the PDP running - to avoid cold starts.
We don't want that authorization queries and requests to the PDP will fail or take a long time because of cold starts.

![Auto Scaling](../images/gcp/3.png)

### 4. Set the container port
Our PDP image runs on port `7000`, so we need to set the container port to `7000`.

![Container Port](../images/gcp/4.png)

### 5. Set the environment variables
Now, we need to set the environment variables for the PDP.
The only required environment variable is `PDP_API_KEY`, which is the API key that you got from Permit.io.
See [Get your API Key](/api/api-with-cli) for more information.
Note that you can and should set the environment variables from a secret, using your selected secret store provider.

![Environment Variables](../images/gcp/5.png)

### 6. Ready to deploy !
Now, we are ready to deploy the PDP.
Click on the "Create" button to deploy the PDP.
You can see the logs of the deployment in the "Logs" tab, and if the deployment succeeded, you will see the URL of the PDP in the top section of the Cloud Run service.

![Deploy](../images/gcp/6.png)


## YAML file
We shared the YAML file that we used to deploy the PDP on GCP Cloud Run.
Take a look at the file `cloud-run.yaml`.

## Signal 6 in Cloud Run
A common misconfiguration issue that can be encountered when deploying the PDP to Google Cloud Run is  having the platform unexpectedly terminate the PDP container with a Signal 6 (SIGABRT). This issue stems from Cloud Run's CPU allocation settings, which allow background task processes, such as the PDP, to release CPU resources when idle. Consequently, this results in the container's termination due to insufficient CPU availability.
To address this issue and ensure uninterrupted service, we recommend adding the `run.googleapis.com/cpu-throttling: false` annotation in the YAML configuration.

For a deeper understanding of CPU allocation settings in Cloud Run and how they impact your applications, please refer to the following documentation: [Cloud Run CPU Allocation Settings](https://cloud.google.com/run/docs/configuring/cpu-allocation).Read here for more information about CPU allocation settings in Cloud Run - https://cloud.google.com/run/docs/configuring/cpu-allocation
