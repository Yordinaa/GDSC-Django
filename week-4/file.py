# Create a Python script that identifies and collects files (both created and modified) in the last 24 hours from the current directory. Update these files in some way and move them to a folder named "last_24hours."

# Requirements:

# Listing Files:
# Use the os module to list all files in the current directory.
# Identification of Files:
# Implement a function to determine whether a file has been created or modified in the last 24 hours.
# Consider both the modification time (st_mtime) and creation time (st_ctime) of the file.

# Update Files:
# Create a function to update the identified files. For example, append a timestamp to the content of each file.

# Create "last_24hours" Folder:
# Check if a folder named "last_24hours" exists. If not, create it using the os module.

# Move Files:
# Move the identified and updated files to the "last_24hours" folder using different method
# Combine the functions to achieve the main objective.



import os
import shutil
from datetime import datetime, timedelta

def list_files(directory="."):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def is_recently_modified_or_created(file_path):
    file_stat = os.stat(file_path)
    
    time_difference = datetime.now().timestamp() - max(file_stat.st_mtime, file_stat.st_ctime)
    
    return time_difference < 24 * 3600

def update_files(files):
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        with open(file_path, 'a') as f:
            f.write("\nUpdated at: " + str(datetime.now()))

def create_last_24hours_folder():
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_files_to_last_24hours(files):
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        destination_path = os.path.join(os.getcwd(), "last_24hours", file)
        shutil.move(file_path, destination_path)

def main():
    files_in_current_directory = list_files()

    recent_files = [file for file in files_in_current_directory if is_recently_modified_or_created(file)]

    create_last_24hours_folder()

    update_files(recent_files)

    move_files_to_last_24hours(recent_files)

if __name__ == "__main__":
    main()
