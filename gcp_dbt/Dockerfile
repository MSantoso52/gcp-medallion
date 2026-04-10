FROM ghcr.io/dbt-labs/dbt-bigquery:1.7.2

# Install dependencies for the gcloud installer
RUN apt-get update && apt-get install -y curl python3

# Install Google Cloud SDK
RUN curl -sSL https://sdk.cloud.google.com | bash

# Add gcloud to the PATH for all future shells
ENV PATH $PATH:/root/google-cloud-sdk/bin

# Verify installation during build
RUN gcloud --version
