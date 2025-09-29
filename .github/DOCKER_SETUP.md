# Docker Build and Publish Setup

This repository includes a GitHub Actions workflow that automatically builds and publishes Docker images to DockerHub.

## Configuration Required

To enable the Docker publishing workflow, you need to configure the following secrets in your GitHub repository:

### Setting up DockerHub Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:

   - **DOCKERHUB_USERNAME**: Your DockerHub username
   - **DOCKERHUB_TOKEN**: Your DockerHub access token (not your password!)

### Creating a DockerHub Access Token

1. Log in to [Docker Hub](https://hub.docker.com/)
2. Go to **Account Settings** → **Security**
3. Click **New Access Token**
4. Give it a descriptive name (e.g., "GitHub Actions")
5. Copy the token and save it as the `DOCKERHUB_TOKEN` secret

## Workflow Triggers

The workflow is triggered automatically on:

- **Push to main/master branch**: Builds and pushes with branch name and `latest` tags
- **Push tags matching `v*`**: Builds and pushes with semantic version tags (e.g., `v1.0.0`, `v1.0`, `v1`)
- **Pull requests**: Builds only (does not push to DockerHub)
- **Manual trigger**: Via the Actions tab in GitHub

## Image Tags

The workflow automatically creates the following tags:

- `latest` - Latest commit on the default branch
- `main` or `master` - Branch name tags
- `v1.0.0`, `v1.0`, `v1` - Semantic version tags (for version tag pushes)
- `pr-123` - Pull request number (for PRs)

## Multi-Platform Support

The workflow builds images for multiple platforms:
- `linux/amd64` (Intel/AMD 64-bit)
- `linux/arm64` (ARM 64-bit, including Apple Silicon)

## Using the Published Images

Once published, you can pull the image using:

```bash
docker pull docker.io/wang-haoxian/reddit-mcp:latest
```

Or use it in your docker-compose.yml:

```yaml
services:
  reddit-mcp:
    image: wang-haoxian/reddit-mcp:latest
    # ... rest of your configuration
```
