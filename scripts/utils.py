import json
import os

# Fungsi untuk menyimpan data ke file JSON
def save_data(data, filename="data/raw_data.json"):
    # Pastikan folder data ada
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Menyimpan data ke file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data berhasil disimpan di {filename}")
