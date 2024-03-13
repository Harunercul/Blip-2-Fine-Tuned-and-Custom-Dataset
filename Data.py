import pandas as pd
import os
from PIL import Image
import io

# Excel dosyasından 'Image_ID' ve 'Caption' sütunlarını yükle
df = pd.read_excel("training_data.xlsx", usecols=["Image_ID", "Caption"])

# Image_ID'ye göre sırala
df.sort_values(by="Image_ID", inplace=True)

# Fotoğrafların bulunduğu klasörü belirt
image_folder = "train_images"

# Veri çerçevesini oluştur
data = {"image": [], "text": []}

# 'Image_ID' sırasına göre fotoğrafları ve açıklamaları ekle
for image_id, caption in zip(df["Image_ID"], df["Caption"]):
    image_path = os.path.join(image_folder, f"image{image_id}.jpg")
    with open(image_path, "rb") as f:
        image_bytes = f.read()  # Görüntüyü byte halinde oku
    data["image"].append(image_bytes)  # Byte'ları ekle
    data["text"].append(caption)

# Veriyi parquet formatında kaydet
parquet_df = pd.DataFrame(data)
parquet_df.to_parquet("veriler100.parquet", index=False)
