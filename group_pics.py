import os
import face_recognition
import cv2
import shutil  # importing the shutil library
import json
# Create a dictionary to store face encodings
face_encodings = {}
# Loop over the images in the directory
image_dir = os.getcwd()+"\\..\\Cropped_pics"

known_dir = os.getcwd()+"\\..\\demo"

known_encodings = []

for filename in os.listdir(known_dir):
    image_path = os.path.join(known_dir, filename)
    image = cv2.imread(image_path)

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Get the face encodings for the image
    face_locations = face_recognition.face_locations(rgb_image, model='cnn')
    if len(face_locations) > 0:
        print(face_locations, filename)
        encodings = face_recognition.face_encodings(rgb_image, face_locations)[0]
        known_encodings.append(encodings)

for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(image_dir, filename)
        image = cv2.imread(image_path)

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get the face encodings for the image
        face_locations = face_recognition.face_locations(rgb_image, model='cnn')
        if len(face_locations) > 0:
            print(face_locations,filename)
            encodings = face_recognition.face_encodings(rgb_image, face_locations)
            face_encodings[filename] = encodings
#Create a list to store the grouped images
grouped_images = []
# Loop over the face encodings and group the images
for i in range (0,len(known_encodings)):
    grouped_images.append([]);

for filename, encodings in face_encodings.items():
    cnt = 0
    for encoding in encodings:
# Check if the encoding matches any of the previous groupings
        distances = face_recognition.face_distance(known_encodings, encoding)
        closest_match_index = distances.argmin()
        if distances[closest_match_index]<= 0.5:
            grouped_images[closest_match_index].append({"filename":filename,"encoding":encoding})

# # Loop over the grouped images and display the faces
cnt = 0
Encodings=[]
for group in grouped_images:
    folder_name = f'people_{cnt}'
    num = 0
    for image in group:
        image_name = image['filename']
        src_path = f'{image_dir}\\{image_name}'
        dir_path = os.getcwd()+"\\..\\"+"All_Faces"+"\\"+folder_name
        if not os.path.exists(dir_path):
            # create the directory if it does not exist
            os.makedirs(dir_path)
        dest_path = dir_path + "\\" + f'people_{cnt}_{num}.jpg'
        num = num + 1
      # copying the picture from source to destination
        shutil.copy(src_path, dest_path)
    my_object = {"class": cnt, "encoding":group[0]['encoding'].tolist()}
    cnt = cnt + 1
    Encodings.append(my_object)
with open("my_list.json", "w") as f:
    json.dump(Encodings, f)