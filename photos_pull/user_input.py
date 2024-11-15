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

if __name__ == "__main__":
  txt_file = input("Enter the path to the text file containing image names: ")
  source_folder = input("Enter the path to the source folder: ")
  destination_folder = input("Enter the path to the destination folder: ")

  copy_images_from_txt(txt_file, source_folder, destination_folder)