import os
import shutil

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

# Loop through all items in Downloads
for item in os.listdir(downloads):
    item_path = os.path.join(downloads, item)

    if os.path.isdir(item_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(item)
    ext = ext.lower()

    moved = False
    for folder_name, extensions in folders.items():
        if ext in extensions:
            dest_folder = os.path.join(downloads, folder_name)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.move(item_path, os.path.join(dest_folder, item))
            moved = True
            break

    # if a file extension I have not accounted for, move to others
    if not moved:
        dest_folder = os.path.join(downloads, "Others")
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        shutil.move(item_path, os.path.join(dest_folder, item))
