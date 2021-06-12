import os
import shutil
import time
def main():
    dfc=0
    dic=0
    path="/PATH_TO_DELETE"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds<=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                dfc+=1
                break
            else:
                 for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds<=get_file_or_folder_age(root_folder):
                        remove_folder(root_folder)
                        dfc+=1
                  for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds<=get_file_or_folder_age(file_path)):
                        remove_folder(file_path)
                        dic+=1
    else:
        if seconds >= get_file_or_folder_age(path):  
            remove_file(path)
            dic+=1
            else:                   
                print(f'"{path}" is not found') dic += 1

                print(f"totalfilesdeleted:{dic}")

                  print(f"totalfolderdeleted:{dfc}")
def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
          else:
             print("Unable to delete the "+path)
def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
      return ctime
if __name__ == '__main__':
    main()