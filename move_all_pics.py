import os
import shutil

current_directory = os.getcwd()
source_dir =os.path.join(current_directory,'afw')
dest_dir = os.path.join(current_directory,'images')
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
image_list = []
cnt = 0
for file_name in os.listdir(source_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        source_path = os.path.join(source_dir, file_name)
        print(file_name)
        image_name=file_name.split('_')[0]+".jpg"
        cnt=cnt+1
        if image_name not in image_list:
            new_filename = image_name
            dest_path = os.path.join(dest_dir, new_filename)
            shutil.copy(source_path, dest_path)
            image_list.append(image_name)
print(len(image_list))
print(cnt)