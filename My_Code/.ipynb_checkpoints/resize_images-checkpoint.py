import cv2
import os
import numpy as np

#modified from https://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images[filename] = img
    return images

def main():
    imgs = load_images_from_folder('to_resize')
    for filename, img in imgs.items():
        dimensions = (int(img.shape[1] / 10), int(img.shape[0] / 10))
        img_resized = cv2.resize(img, dimensions, interpolation = cv2.INTER_AREA)
        file_prefix = filename[0:filename.find(".")]
        cv2.imwrite("resized/" + file_prefix + "_resized.jpg", img_resized)

main()