import os

path = r'/home/USERNAME/Downloads'

# Lists all files in the directory
files = (file for file in os.listdir(path)
        if os.path.isfile(os.path.join(path, file)))

for file in files:
    filename_split = file.split(".")
    extension = filename_split[len(filename_split) - 1]

    extension_folder_name = path + "//" + extension
    if not os.path.exists(extension_folder_name):
        os.makedirs(extension_folder_name)

    os.rename(path + "//" + file, extension_folder_name + "//" + file)