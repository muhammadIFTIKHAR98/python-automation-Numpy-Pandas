
#!/usr/bin/env python3
import os     #a standard library that allows interaction with the operating system. It provides functions for file operations, directory management, and other OS-related tasks. 
              #You can use it to perform actions like creating, deleting, and renaming directories, accessing file paths, and running shell commands. 

import shutil   #Shutil module in Python provides many functions of high-level operations on files and collections of files. It comes under Python’s standard utility modules.
                #This module helps in automating the process of copying and removing files and directories.

'''define the source directory (where files are located) 
and the target directory for each filetype'''

source_dir = '/path/to/files/which/are/downloaded' #path to download folder

#mapping file types to destination folders. Defining File Extensions for Categorization.
file_extension = {
    "images": ['.jpg', '.png', '.jpeg', '.gif', '.bmp'],
    "documents": ['.pdf', '.docx', '.txt', '.xlsx'],
    "videos": ['.mp4', '.avi', '.mov', '.mkv'],
    "music": ['.mp3', '.wav', '.flac'],
}
'''
Defining the function to organize files
This is the main function that organizes files. It:
        Iterates through the files in the source folder.
        Checks their extensions.
        Moves them to the appropriate subfolder.
'''
def organize_files():
    source_folder = os.listdir(source_dir)    # This will lists all the files and directories present in the source_dir.
    for filename in source_folder:            # This will loop/iterate through each file present in source_folder
        # get file extension and full path
        file_path = os.path.join(source_dir, filename)    # By joining the sorce_dir and filename we will get the full file path.

      
        if os.path.isfile(file_path):         # This ensures that item is a file and not a folder.
            file_ext = os.path.splitext(filename)[1].lower()   # This will split the filename into two parts "file" and ".jpg", then we will select the second part(index [1]) and keep it in lower state. 
            print(f"processing file: {filename}, extension: {file_ext}") #debug output

            #find the appropriate folder based on file extension
            folder_name = "others"            # This is where all files go if their extension does not match with provided extensions in file_extension.
            for folder, extension in file_extension.items():      # Loop through each category in the file_extension dictonary
                if file_ext in extension:                         
                    folder_name = folder      # This will give folder_name the name provided in the file_extension dictonary, to be precise key of dictonary.
                    break                     # Stops the loop when match is found. this make code efficient because it doesn't keep searching unnecessarily.

            #debug: show where the file is going
            print(f"moving {filename} to folder: {folder_name}") #debug output    

            #create the folder if it doesn't exist
            target_folder = os.path.join(source_dir, folder_name)
            if not os.path.exists(target_folder):                  # This condition will be fullfilled when the code runs first time with unique extension after that it will exist
                os.makedirs(target_folder)                         # This will create the target_folder if it doesn't exist, which will happen only when code is run first time or extension is unique.

            #move the file to the appropriate folder
            shutil.move(file_path, target_folder)
            print(f"moved {filename} to {folder_name}")

#run the organizer
if __name__ == "__main__":
    organize_files()
    print("file organization complete!")
