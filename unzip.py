import os
import zipfile

# Get the current directory
current_directory = os.getcwd()

# List all files in the current directory
files = os.listdir(current_directory)

# Loop through each file
for file in files:
    # Check if the file is a zip file
    if file.endswith('.zip'):
        # Create a full file path
        file_path = os.path.join(current_directory, file)
        
        # Create a folder name by removing the '.zip' extension
        folder_name = file[:-4]
        
        # Create a folder to extract the zip contents
        os.makedirs(folder_name, exist_ok=True)
        
        # Open the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Extract all contents to the folder
            zip_ref.extractall(folder_name)
            
        print(f"Extracted '{file}' to '{folder_name}' folder.")
