
#!/usr/bin/env python3
import os
import shutil

'''define the source directory (where files are located) 
and the target directory for each filetype'''

source_dir = '/path/to/download/files' #path to download folder

#mapping file types to destination folders
file_extension = {
    "images": ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
    "documents": ['.pdf', '.docx', '.txt', 'xlsx'],
    "videos": ['.mp4', '.avi', '.mov', 'mkv'],
    "music": ['.mp3', '.wav', 'flac'],
}

#function to organize files
def organize_files():
    for filename in os.listdir(source_dir):
        # get file extension and full path
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower() #file extension
            print(f"processing file: {filename}, extension: {file_ext}") #debug output

            #find the appropriate folder based on file extension
            folder_name = "others"
            for folder, extension in file_extension.items():
                if file_ext in extension:
                    folder_name = folder
                    break

            #debug: show where the file is going
            print(f"moving {filename} to folder: {folder_name}") #debug output    

            #create the folder if it doesn't exist
            target_folder = os.path.join(source_dir, folder_name)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            #move the file to the appropriate folder
            shutil.move(file_path, target_folder)
            print(f"moved {filename} to {folder_name}")

#run the organizer
if __name__ == "__main__":
    organize_files()
    print("file organization complete!")
