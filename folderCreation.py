import os

def create_folders(base_path, folder_names):
    try:
        for folder in folder_names:
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            print(f'Folder "{folder}" created at {folder_path}')
    except Exception as e:
        print(f"An error occurred: {e}")


base_path = '/Users/muhammedshahidchammayil/'
folder_names = ['Thank you', 'For', 'Considering', 'My Application']
create_folders(base_path, folder_names)