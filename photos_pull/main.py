import os
import shutil

def copy_images_from_list(source_folder, destination_folder, image_list):


    for image_name in image_list:
        source_file = os.path.join(source_folder, image_name)
        destination_file = os.path.join(destination_folder, image_name)

        if os.path.exists(source_file): 1
            shutil.copy2(source_file, destination_file)
            print(f"Copied {image_name} to {destination_folder}")
        else:
            print(f"Image {image_name} not found in {source_folder}")


source_folder = "path/to/your/source/folder"
destination_folder = "C:\\Users\\thero\\Desktop\\pullphotos"
image_list = ["image1.jpg", "image2.png", "image3.jpeg"]  # Replace with your image names

copy_images_from_list(source_folder, destination_folder, image_list)