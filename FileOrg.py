import os
import shutil

# Define the folder to organize
folder_to_organize = "Desktop/Abhijit"

# Define file type categories and their corresponding extensions
file_categories = {
    "Images": ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Music": ['.mp3', '.wav', '.flac'],
    "Videos": ['.mp4', '.mkv', '.flv', '.avi'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
}

# Create folders if they do not exist
def create_folders(folder_path, categories):
    for category in categories:
        folder = os.path.join(folder_path, category)
        if not os.path.exists(folder):
            os.makedirs(folder)

# Organize files
def organize_files(folder_path, categories):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        file_extension = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                # Move the file to the respective folder
                shutil.move(file_path, os.path.join(folder_path, category, filename))
                moved = True
                break

        # If file extension does not match any category, move to 'Others' folder
        if not moved:
            other_folder = os.path.join(folder_path, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))

# Run the file organizer
create_folders(folder_to_organize, file_categories)
organize_files(folder_to_organize, file_categories)

print("Files organized successfully.")
