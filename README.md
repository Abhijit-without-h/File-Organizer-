
---

# Python File Organizer

This is a simple Python script that organizes files in a specified directory by sorting them into folders based on their file extensions. It helps to keep your files tidy by categorizing them into directories such as `Images`, `Documents`, `Music`, `Videos`, and more.

## Features
- Automatically categorizes files by type (e.g., images, documents, music, videos, archives).
- Creates folders for each file type (if they don't already exist).
- Moves files into the respective folders based on their extensions.
- If a file's extension doesn't match a predefined category, it's moved to an `Others` folder.

## Prerequisites

- Python 3.x
- Basic understanding of how to run Python scripts

### Installation (Optional)
You can install the required dependencies (if any) using:
```bash
pip install -r requirements.txt
```
_Note: This script does not have any additional dependencies beyond Python's standard library._

## Usage

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. Replace the value of `folder_to_organize` in the script with the absolute path to the folder you want to organize:

   ```python
   folder_to_organize = "/path/to/your/folder"
   ```

3. Run the Python script:

   ```bash
   python3 file_organizer.py
   ```

4. The files in the specified folder will be moved into new directories based on their type.

### Example:
If you have the following files in `/Users/yourname/Documents/`:
```
photo.jpg
song.mp3
report.pdf
```
After running the script, the `Documents` folder will be organized like this:
```
Documents/
    Images/
        photo.jpg
    Music/
        song.mp3
    Documents/
        report.pdf
```

## File Categories

By default, the script categorizes the following file types:

- **Images**: `.jpeg`, `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- **Music**: `.mp3`, `.wav`, `.flac`
- **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`
- **Archives**: `.zip`, `.rar`, `.tar`, `.gz`
- **Others**: Files that don't match any of the above categories.

## Customization

You can easily modify the script to handle additional file types or change the file categories by editing the `file_categories` dictionary in the script.

For example, to add a new category for Python scripts:

```python
"Python Scripts": ['.py']
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
Feel free to modify or extend this **README** to include more specific instructions or details relevant to your project!
