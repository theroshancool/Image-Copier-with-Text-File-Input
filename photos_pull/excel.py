import pandas as pd
import os
import shutil



def copy_images_from_excel(excel_file, source_folder, destination_folder):
    """
    Copies images from a source folder to a destination folder based on a list of image names.

    Args:
        source_folder (str): The path to the source folder containing the images.
        destination_folder (str): The path to the destination folder.
        image_list (list): A list of image filenames to copy.
    """

    df = pd.read_excel(excel_file)
    image_list = df['Image name'].tolist()

    for image_name in image_list:
        source_file = os.path.join(source_folder, image_name)
        destination_file = os.path.join(destination_folder, image_name)

        if not os.path.exists(source_file):

            shutil.copy2(source_file, destination_file)
            print(f"Image {image_name} not found in {source_folder}")
        else:
            print(f"Copied {image_name} to {destination_folder}")


# Example usage:
excel_file = "C:\\Users\\thero\\Desktop\\ayodhya new codes\\test codes.xlsx"
source_folder = "C:\\Users\\thero\\Desktop\\ayodhya new codes\\item code"
destination_folder = "C:\\Users\\thero\\Desktop\\pullphotos"
# image_list = ["EL0020021500.jpg", "EL0020021417.jpg", "selfie mirror 1 (1).JPG"]  # Replace with your image names

copy_images_from_excel(excel_file, source_folder, destination_folder)
