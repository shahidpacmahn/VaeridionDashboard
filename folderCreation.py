import os

def create_folders(base_path, folder_names):
    try:
        for folder in folder_names:
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            print(f'Folder "{folder}" created at {folder_path}')
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
base_path = '/Users/muhammedshahidchammayil/'
folder_names = ['Folder1', 'Folder2', 'Folder3', 'Folder4']
create_folders(base_path, folder_names)