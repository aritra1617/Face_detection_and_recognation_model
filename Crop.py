import json
import os
import cv2
# Open the file

json_dir = os.getcwd()+"\\..\\result.json"
cropped_pic_dir= os.getcwd()+"\\..\\Cropped_pics"

if not os.path.exists(cropped_pic_dir):
    os.makedirs(cropped_pic_dir)

with open(json_dir) as f:
    # Load the JSON data
    json_data = json.load(f)

# Access the data
for data in json_data:
    print(data)
    # Load the image
    image_name=os.getcwd()+"\\..\\"+data['filename']
    img = cv2.imread(image_name)
    height, width = img.shape[:2]
    cnt = 0
    # Set the coordinates for the bounding box (left, upper, right, lower)
    for object in data['objects']:
        center_x=int(object['relative_coordinates']['center_x']*width)
        center_y = int(object['relative_coordinates']['center_y']*height)
        wid = int(object['relative_coordinates']['width']*width)
        ht = int(object['relative_coordinates']['height']*height)
        x,y,w,h=center_x-wid//2,center_y-ht//2,wid,ht
        cropped_filename = cropped_pic_dir+"\\" +data['filename'].split('/')[1].split('.')[0]+"_"+str(cnt)+".jpg"
        #print(cropped_filename)
        cropped_img = img[y:y + h, x:x + w]
        cv2.imwrite(cropped_filename, cropped_img)
        cnt = cnt + 1
    # Display the cropped image
        #cv2.imshow('Cropped Image', cropped_img)
        #cv2.waitKey(0)
