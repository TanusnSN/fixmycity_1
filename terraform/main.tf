terraform {
  required_version = ">= 1.5.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# Pull or manage the Docker image for FixMyCity
resource "docker_image" "fixmycity" {
  name         = "fixmycity:latest"
  keep_locally = true
}

# Run the FixMyCity container
resource "docker_container" "fixmycity_container" {
  image = docker_image.fixmycity.image_uri
  name  = "fixmycity-prod"

  ports {
    internal = 8000
    external = 8080
  }

  env = [
    "ENVIRONMENT=production"
  ]

  restart = "unless-stopped"
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.fixmycity_container.id
}

output "app_url" {
  description = "URL to access the production container"
  value       = "http://localhost:8080"
}