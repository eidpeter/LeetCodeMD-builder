import os

class FileHandler:
    def __init__(self):
        pass

    def create_folder(self, path, folder_name):
        folder_path = os.path.join(path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path

    def create_file(self, path, file_name):
        file_path = os.path.join(path, file_name)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

        return file_path