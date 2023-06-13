import os
import cv2
import shutil
import json
import face_recognition
import numpy as np

current_directory = os.getcwd()
All_pics_directory = current_directory + "\\..\\"+"video_pics"
result_json_dir = current_directory + "\\..\\result.json"
dataset_dir = current_directory + "\\..\\"+"Dataset"
class_cnt = 0

if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)


with open(result_json_dir) as f:
    json_data = json.load(f)
with open('my_list.json') as f:
    my_list = json.load(f)

All_valid_pics = []
try:
    for data in json_data:

        image_name=data["filename"].split("/")[1]

        image_filename = os.path.join(All_pics_directory,image_name)
        img = cv2.imread(image_filename)
        height, width = img.shape[:2]

        txt_filename=dataset_dir +"\\" +image_name.split(".")[0]+".txt"

        with open(txt_filename,'w') as f:

            for object in data["objects"]:

                center_x=int(object['relative_coordinates']['center_x']*width)
                center_y = int(object['relative_coordinates']['center_y']*height)
                wid = int(object['relative_coordinates']['width']*width)
                ht = int(object['relative_coordinates']['height']*height)
                x,y,w,h=center_x-wid//2,center_y-ht//2,wid,ht

                cropped_img = img[y:y + h, x:x + w]
                rgb_image = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
                # Get the face encodings for the image
                face_locations = face_recognition.face_locations(rgb_image, model='cnn')
                if len(face_locations) > 0:
                    encodings = face_recognition.face_encodings(rgb_image, face_locations)
                    for encoding in encodings:
                        for list in my_list:
                            if face_recognition.compare_faces([np.array(list['encoding'])], encoding,tolerance=0.5)[0]:
                                class_name = list['class']
                                print(class_name)
                                bbox_center_x = object['relative_coordinates']['center_x']
                                bbox_center_y = object['relative_coordinates']['center_y']
                                bbox_width = object['relative_coordinates']['width']
                                bbox_height = object['relative_coordinates']['height']
                                if f'data/Test/{image_name}\n' not in All_valid_pics:
                                    All_valid_pics.append(f'data/Test/{image_name}\n')
                                f.write(f'{class_name} {bbox_center_x} {bbox_center_y} {bbox_width} {bbox_height}\n')
                                break

        f.close()
except:
    print("error")
with open(os.path.join(dataset_dir,'image_data.data'),'w') as f:
        f.write(f'classes = {len(my_list)}\n')
        f.write('train = data/Test/train.txt\n')
        f.write('valid = data/Test/test.txt\n')
        f.write('backup = backup_test\n')
        f.write('names = data/Test/classes.names\n')

with open(os.path.join(dataset_dir,"train.txt"),'w') as train:
    for path in All_valid_pics:
        train.write(path)
        src_path = (All_pics_directory + "\\" + path.split('/')[2]).split("\n")[0]
        des_path = (dataset_dir + "\\" + path.split('/')[2]).split("\n")[0]
        shutil.copy(src_path,des_path)

with open(os.path.join(dataset_dir,"classes.names"),'w') as c:
    with open(os.path.join(dataset_dir,"classes.txt"),'w') as cl:
        for i in range(0,len(my_list)):
            cl.write(f'people_{i}\n')
            c.write(f'people_{i}\n')
    cl.close()
c.close()