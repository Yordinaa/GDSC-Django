import os
import datetime

TARGET_FOLDER = 'last_24hours'

def get_files():
   return os.listdir('.')
   
def is_recent(filename):
   path = os.path.join('.', filename)
   modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))
   creation_time = datetime.datetime.fromtimestamp(os.path.getctime(path))
   
   now = datetime.datetime.now()
   
   if (now - modification_time).total_seconds() < 86400 and (now - creation_time).total_seconds() < 86400:
      return True
   else:  
      return False
def update_file(filename):
   try:
      with open(filename, 'a') as f:
         f.write(f"\nUpdated at: {datetime.datetime.now()}")
   except PermissionError:    
      print(f"No access to {filename}, skipping")
      print(filename)
def create_folder():
   if not os.path.exists(TARGET_FOLDER):
      os.makedirs(TARGET_FOLDER)
def move_file(filename):

   source = os.path.join('.', filename) # set source path

   if not os.path.exists(TARGET_FOLDER):
      try:
         os.makedirs(TARGET_FOLDER)  
      except OSError as e:
         print(f"Folder creation error: {e}")
         return

   destination = os.path.join(TARGET_FOLDER, filename)
   
   try:   
      os.replace(source, destination)
   except OSError as e:
      print(f"File move error: {e}")
if __name__ == '__main__':

   create_folder()
   
   files = get_files()  
   
   for file in files:

      if is_recent(file):
         
         update_file(file)
         
         move_file(file)
         
   print("Files processed")
