resource "google_storage_bucket" "master-list-code-storage-bucket" {
  name                        = "zerodha-master-list-code"
  uniform_bucket_level_access = true
  storage_class               = "Standard"
  location                    = var.google_cloud_project_region
}