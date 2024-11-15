import os
import shutil

def copy_images_from_txt(txt_file, source_folder, destination_folder):


  with open(txt_file, 'r') as f:
    image_list = f.read().splitlines()

  for image_name in image_list:
    source_file = os.path.join(source_folder, image_name)
    destination_file = os.path.join(destination_folder, image_name)

    try:
      shutil.copy2(source_file, destination_file)
      print(f"Copied {image_name} to {destination_folder}")
    except (shutil.Error, OSError) as e:
      print(f"Error copying {image_name}: {e}")

# Example usage:
txt_file = "C:\\Users\\thero\\Desktop\\ayodhya new codes\\test.txt"
source_folder = "C:\\Users\\thero\\Desktop\\ayodhya new codes\\item code"
destination_folder = "C:\\Users\\thero\\Desktop\\pullphotos"

copy_images_from_txt(txt_file, source_folder, destination_folder)