# organize the download folder
# move images, documents, zip files 
# into corresponding folders
# File extensions
import os
import shutil


img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif")
document = (".pdf")
zip_files = (".zip")

# Helper functions
def is_image(file):
    return os.path.splitext(file)[1].lower() in img

def is_document(file):
    return os.path.splitext(file)[1].lower() in document

def is_zip(file):
    return os.path.splitext(file)[1].lower() in zip_files

# Change directory to Downloads
os.chdir('C:/Users/bunty/Downloads')

# Iterate over files in Downloads
for file in os.listdir():
    if is_image(file):
        shutil.move(file, 'C:/Users/bunty/Desktop/imgs_downloads')
    elif is_document(file):
        shutil.move(file, 'C:/Users/bunty/Desktop/docs_downloads')
    elif is_zip(file):
        shutil.move(file, 'C:/Users/bunty/Desktop/zip_downloads')