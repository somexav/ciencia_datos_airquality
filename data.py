import kagglehub

# Download latest version
path = kagglehub.dataset_download("global-air-quality-and-deforestation-dataset")

print("Path to dataset files:", path)