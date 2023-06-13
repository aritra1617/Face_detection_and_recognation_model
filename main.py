import os
import numpy as np
# load image and .pts file
import glob
import cv2
current_directory = os.getcwd()
directory = current_directory +"\\..\\"+"Cropped_pics"
pts_files = []
cnt = 0
for filename in glob.glob(directory + '/*.pts'):
    pts_files.append(filename)

for pts_file in pts_files:
    with open(pts_file, "r") as f:
        lines = f.readlines()
    filename = pts_file.split('\\')[5].split('_')[0]+".txt"
    image_path = pts_file.split('.')[0]+".jpg"
    print(image_path)
    img = cv2.imread(image_path)
    height, width,channels = img.shape
    # parse .pts file to extract facial landmark coordinates
    landmarks = []
    for line in lines[3:-1]:
        x, y = map(float, line.split())
        landmarks.append([x, y])
    landmarks = np.array(landmarks)
    # compute bounding box coordinates
    x_min = np.min(landmarks[:, 0])
    x_max = np.max(landmarks[:, 0])
    y_min = np.min(landmarks[:, 1])
    y_max = np.max(landmarks[:, 1])
    center_x = (x_min+x_max)/2
    center_y = (y_min+y_max)/2
    center_x = center_x/width
    center_y = center_y/height
    width = int(x_max - x_min+1)/width
    height = int(y_max - y_min +1)/height
    annotation_filename = os.path.join(os.path.join(current_directory,'annotations'),filename)
    with open(annotation_filename,'a') as f:
        f.write(f"{0} {center_x} {center_y} {width} {height}\n")
