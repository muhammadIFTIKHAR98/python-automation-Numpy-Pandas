import os
import shutil
from datetime import datetime

#define the source and backup directories
source_dir = "/path/to/source/directory"  #the directory you want to back up
backup_dir = "/path/to/backup/destination/directory"   #where the backup will be saved

#create a new directory with a timestamp for each backup
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
backup_subdir = os.path.join(backup_dir, f"backup_{current_time}")

#ensure the backup directory exists
if not os.path.exists(backup_subdir):
    os.makedirs(backup_subdir)

def backup_files():
    #loop through all files and directories in the source folder
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        backup_item = os.path.join(backup_subdir, item)

        #if it's a file copy it
        if os.path.isfile(source_item):
            shutil.copy2(source_item, backup_item)

        #if it's a directory, copy the entire directory
        elif os.path.isdir(source_item):
            shutil.copytree(source_item, backup_item)

    print(f"backup completed successfully at {backup_subdir}")

#run the backup process
backup_files()
