# Load dataset from Kaggle
 !pip install kagglehub
 
 import kagglehub

## Download latest version
path = kagglehub.dataset_download("ziya07/power-converters-in-electric-vehicles-dataset")

print("Path to dataset files:", path)
