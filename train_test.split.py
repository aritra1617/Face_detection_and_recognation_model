import os
import random
current_directory = os.getcwd()
source_dir =os.path.join(current_directory,'All_Files')
total_images = []
for file_name in os.listdir(source_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        total_images.append(file_name)
num_samples = int(len(total_images) * 40 / 100)
validation_set = random.sample(total_images, num_samples)
train_set=[]
for file in total_images:
    if file not in validation_set:
        train_set.append(file)
test_path = os.path.join(os.path.join(current_directory,'All_Files'),'test.txt')
train_path=os.path.join(os.path.join(current_directory,'All_Files'),'train.txt')
with open(test_path,'w') as f:
    for file in validation_set:
        file_name=f"data/Test/{file}"
        f.write(file_name+"\n")
with open(train_path,'w') as f:
    for file in train_set:
        file_name=f"data/Test/{file}"
        f.write(file_name+"\n")
