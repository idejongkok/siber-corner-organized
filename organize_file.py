import os
import shutil

def organize_files(source_dir,target_dir):
    files = os.listdir(source_dir)
    
    for file in files:
        source_path = os.path.join(source_dir,file)
        
        if os.path.isfile(source_path):
            
            x, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()
            
            target_folder_path = f'{target_dir}/{file_extension[1:]}'
            
            os.makedirs(target_folder_path, exist_ok=True)
            
            target_path = f'{target_folder_path}/{file}'
            print(target_path)
            
            shutil.move(source_path, target_path)
            
            print(f'file {file} dipindahin ke folder {file_extension[1:]}.')

if __name__ == "__main__":
    source_dir = 'C:/Users/susen/Downloads'
    target_dir = 'C:/Users/susen/Downloads/Org'
    organize_files(source_dir, target_dir)