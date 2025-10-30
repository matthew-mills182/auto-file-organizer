import os
import shutil
import time

# Establish folder to watch
downloads = r"/mnt/c/Users/mills/Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".rtf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"]
}

def organize_downloads():
    for item in os.listdir(downloads):
        item_path = os.path.join(downloads, item)

        if os.path.isdir(item_path):
            continue

        _, ext = os.path.splitext(item)
        ext = ext.lower()

        moved = False
        for folder_name, extensions in folders.items():
            if ext in extensions:
                dest_folder = os.path.join(downloads, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(item_path, os.path.join(dest_folder, item))
                moved = True
                break

        if not moved:
            dest_folder = os.path.join(downloads, "Others")
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_folder, item))

print("Starting download organizer. Press Ctrl+C to stop.")

try:
    while True:
        organize_downloads()
        time.sleep(5)  # check every 5 seconds
except KeyboardInterrupt:
    print("Organizer stopped.")
