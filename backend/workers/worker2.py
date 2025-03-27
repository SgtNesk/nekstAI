import os
from pathlib import Path

# Directory dei file caricati
UPLOADS_DIR = Path("../uploads")

def collect_data():
    """Simula la raccolta dati da nomeAzienda B."""
    data = []
    if UPLOADS_DIR.exists():
        for file_path in UPLOADS_DIR.iterdir():
            if file_path.is_file():
                file_info = {
                    "filename": file_path.name,
                    "size": file_path.stat().st_size,  # Dimensione in byte
                    "source": "nomeAzienda B"
                }
                data.append(file_info)
    return data

if __name__ == "__main__":
    collected_data = collect_data()
    print("Dati raccolti da nomeAzienda B:")
    for item in collected_data:
        print(item)