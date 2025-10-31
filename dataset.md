# Load dataset from Kaggle

 import kagglehub

## Download latest version
path = kagglehub.dataset_download("ziya07/power-converters-in-electric-vehicles-dataset")

print("Path to dataset files:", path)
