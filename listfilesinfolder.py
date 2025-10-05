import os
def list_files_in_folder(folder_path):
    files=[]
    for file in os.listdir(folder_path):
        files.append(file)
    print(files) 
    
    
list_files_in_folder("/home/muthoni-gathiithi/Documents")
