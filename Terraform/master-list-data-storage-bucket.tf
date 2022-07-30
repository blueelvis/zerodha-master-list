resource "google_storage_bucket" "master-list-data-storage-bucket" {
  name                        = "zerodha-master-list-data"
  uniform_bucket_level_access = true
  storage_class               = "Standard"
  location = var.google_cloud_project_region
}