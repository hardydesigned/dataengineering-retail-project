terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

# Configure the Google Cloud provider
provider "google" {
  project     = var.project_id
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = file(var.credentials)
}

# Create a Google Cloud Storage bucket
resource "google_storage_bucket" "gcs_bucket" {
  name          = var.bucket_name
  location      = "US"
  force_destroy = true # Warning: This will delete the bucket and its contents when destroyed
}

# Create a virtual machine instance
resource "google_compute_instance" "vm_instance" {
  name         = "mage-postgres-vm"
  machine_type = "e2-medium"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "ubuntu-2204-lts"
      size  = 50
      type  = "pd-standard"
    }
  }

  network_interface {
    network = "default"

    access_config {
      # This is required to give the VM a public IP
    }
  }

  tags = ["http-server", "https-server"]
}


# Define variables
variable "project_id" {
  default = "your-project-id"
}

variable "zone" {
  default = "us-central1-a"
}

variable "bucket_name" {
  default = "your-bucket-name"
}

output "vm_instance_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}

variable "credentials" {
  default = "path/to/your/credentials.json"
}

