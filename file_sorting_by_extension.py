import os
import shutil


SOURCE_FOLDER = ''
OUTPUT_FOLDER = ''

for directory_path, sub_directories, file_names in os.walk(SOURCE_FOLDER):
    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1][1:].lower()
            extension_folder = os.path.join(OUTPUT_FOLDER, file_extension)
            destination_path = os.path.join(extension_folder, file_name)

            if not file_path.startswith(extension_folder):
                os.makedirs(extension_folder, exist_ok=True)

                destination_path = os.path.join(extension_folder, file_name)
                i = 2

                while os.path.exists(destination_path):
                    file_name = f"{file_name[:-len(file_extension) - 1]} - copy {i}.{file_extension}"
                    destination_path = os.path.join(extension_folder, file_name)
                    i += 1

                try:
                    shutil.move(file_path, destination_path)
                except Exception as err:
                    print(err)

                print(f"File '{file_path}' moved to {destination_path}")
