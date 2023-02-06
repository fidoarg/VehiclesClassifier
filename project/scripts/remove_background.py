"""
This script will be used to remove noisy background from cars images to
improve the quality of our data and get a better model.
The main idea is to use a vehicle detector to extract the car
from the picture, getting rid of all the background, which may cause
confusion to our CNN model.
We must create a new folder to store this new dataset, following exactly the
same directory structure with its subfolders but with new images.
"""

import argparse
import cv2
import os
from utils import detection
from utils import utils

def parse_args():
    parser = argparse.ArgumentParser(description="Train your model.")
    parser.add_argument(
        "data_folder",
        type=str,
        help=(
            "Full path to the directory having all the cars images. Already "
            "splitted in train/test sets. E.g. "
            "`/home/app/src/data/car_ims_v1/`."
        ),
    )
    parser.add_argument(
        "output_data_folder",
        type=str,
        help=(
            "Full path to the directory in which we will store the resulting "
            "cropped pictures. E.g. `/home/app/src/data/car_ims_v2/`."
        ),
    )

    args = parser.parse_args()

    return args


def main(data_folder, output_data_folder):
    """
    Parameters
    ----------
    data_folder : str
        Full path to train/test images folder.

    output_data_folder : str
        Full path to the directory in which we will store the resulting
        cropped images.
    """
    # For this function, you must:
    #   1. Iterate over each image in `data_folder`, you can
    #      use Python `os.walk()` or `utils.walkdir()``
    #   2. Load the image
    for source_image_dir, source_image_filename in utils.walkdir(data_folder):
        img_source_file_path= os.path.join(
            source_image_dir, source_image_filename
        )
        img= cv2.imread(img_source_file_path)
#   3. Run the detector and get the vehicle coordinates, use
#      utils.detection.get_vehicle_coordinates() for this task
        box_coordinates = detection.get_vehicle_coordinates(img)

#   4. Extract the car from the image and store it in
#      `output_data_folder` with the same image name. You may also need
#      to create additional subfolders following the original
#      `data_folder` structure.
        x1, y1, x2, y2 = box_coordinates
        cropped_img = img[y1:y2, x1:x2, :]

        dest_image_dir = source_image_dir.replace(data_folder, output_data_folder)
        if not os.path.isdir(dest_image_dir):
            os.makedirs(dest_image_dir)
        img_dest_file_path= os.path.join(
            dest_image_dir, source_image_filename
        )
        cv2.imwrite(img_dest_file_path, cropped_img)

if __name__ == "__main__":
    args = parse_args()
    main(args.data_folder, args.output_data_folder)
