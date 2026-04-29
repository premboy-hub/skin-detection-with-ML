import os
import pandas as pd
import shutil

# Paths
csv_path = "HAM10000_metadata.csv"
image_folder_1 = "HAM10000_images_part_1"
image_folder_2 = "HAM10000_images_part_2"
dataset_folder = "dataset"

# Read CSV
data = pd.read_csv(csv_path)

# Create class folders
labels = data['dx'].unique()

for label in labels:
    os.makedirs(os.path.join(dataset_folder, label), exist_ok=True)

# Move images
for index, row in data.iterrows():
    image_name = row['image_id'] + ".jpg"
    label = row['dx']

    src_path = os.path.join(image_folder_1, image_name)
    if not os.path.exists(src_path):
        src_path = os.path.join(image_folder_2, image_name)

    dst_path = os.path.join(dataset_folder, label, image_name)

    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)

print("✅ Dataset Organized Successfully!")