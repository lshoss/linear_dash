import kagglehub

# Download latest version
path = kagglehub.dataset_download("vmohammedraiyyan/maternal-health-and-high-risk-pregnancy-dataset")

print("Path to dataset files:", path)