# Abstract:
The purpose of this project is to develop a face detection and recognition system capable of analyzing video footage and accurately detecting and recognizing faces in real-time. The project utilizes the YOLOv4 object detection algorithm and the ResNeXt deep convolutional neural network architecture to achieve high performance in terms of both detection accuracy and computational efficiency.

# 1. Introduction:
In recent years, face detection and recognition have gained significant attention due to their wide range of applications in various domains such as surveillance, security, and human-computer interaction. The ability to detect and recognize faces from video footage in real-time has become a crucial task. This project aims to address this challenge by combining the power of YOLOv4, a state-of-the-art object detection algorithm, with the ResNeXt architecture, a powerful convolutional neural network for feature extraction.

# 2. Methodology:
## 2.1 YOLOv4:
YOLOv4 (You Only Look Once) is an advanced object detection algorithm that achieves real-time performance by employing a single neural network to predict bounding boxes and class probabilities directly, integrating with a strong backbone like ResNeXt for feature extraction enhances system's capability for complex computer vision tasks.

## 2.2 ResNeXt:
ResNeXt is a deep convolutional neural network architecture that has demonstrated exceptional performance in image classification tasks. It introduces a new block structure called a "cardinality" block, which allows the network to learn rich and diverse feature representations. By incorporating ResNeXt into our project, we aim to enhance the accuracy of face recognition by leveraging the powerful feature extraction capabilities of this architecture.

## Anatomy of detection
There are Three key components in Object detection:

Backbone: The backbone is responsible for extracting features from input image.

Neck: The neck is responsible for fusing the features extracted by the backbone and integrating them into a form that is suitable for detection.

Head: The head is responsible for detecting objects in the image. 

![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/9a2daf2f-654d-434f-903c-88f0555bc4b3)


# 3. Data Collection and Preprocessing:
The success of any machine learning project heavily relies on the availability of high-quality data. Two datasets are utilized in this project, one for training a face detection model, and another for recognizing people in videos.

Face Detection Dataset: we have used ‘Wider Face’ dataset for face detection, which has 32,203 images and registered 393,703 faces with significant variations in scale, position and occlusion. 

![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/dea7d3cf-a5c4-4b32-a05d-d8c52ca8530e)

Video Dataset: We analyzed a 32-second video with three individuals, dividing it into one-second intervals to obtain a total of 32 frames. In these frames, we detected a total of 96 faces, with each person represented in 32 frames.

![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/73a7b67e-c8cd-4524-b2e6-47db4bf84407)


To ensure optimal performance, we preprocessed the dataset by normalizing pixel values, augmenting the data with techniques such as random cropping and flipping, and splitting it into training, validation, and testing sets.

# 4. Model Training:
## 4.1 Face Detection:
* Procedure for Face Detection:
1. Collect dataset: Collect a dataset of images that contain faces to train the model.


2. Annotate the dataset: Annotate with bounding boxes to create a labeled dataset. The YOLOv4 algorithm expects annotations in a specific format, including class id, bounding box center coordinates, and dimensions (height and width).


3. Configure the Hyperparameters: Configure the "csresnext50-panet-spp-original-optimal.cfg" file with appropriate parameters, including the number of classes, anchors, filters, height, width, and batch size.


4. Train the model: Train the model on annotated dataset, This involves specifying the paths to training and validation datasets, the location of the configuration file and the pre-trained weights, and the number of epochs to train the model.

![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/1f9914b1-0425-467e-9ba3-ec6e36f3535b)


## 4.2 Face Recognition:

* Procedure for Face Recognition:

1. Extracting Frames: Utilize the Python OpenCV module to extract one static image per second from the tested video.

2. Face Detection: Employ the previously trained face detection model to detect human faces from extracted frames. Crop the detected faces and store them in the "Cropped_Pics" folder.

3. Face Grouping: Use the Python face_recognition module to group the detected faces belonging to the same person. Save these grouped faces in separate folders labeled as "person_no".

4. Annotation Creation: Generate an annotation file for each image in the YOLOv4 format. Save these annotation files in a dedicated folder.

5. Dataset Preparation: Prepare the resulting dataset to train a face recognition model. Include images of all individuals featured in the video.
![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/ba9e1812-5c0a-441b-b33a-f2cc66caaee5)

# Loss measurement:

The model uses a combination of localization loss, confidence loss, and classification loss to train and optimize the network.

Classification loss: If an object is detected, the classification loss at each cell is the squared error of the class conditional probabilities for each class.

			∑1_(𝑖=0)^(𝑆^2)▒∆_𝑖^𝑜𝑏𝑗  ∑1_(𝑐∈𝑐𝑙𝑎𝑠𝑠𝑒𝑠)▒〖(𝑝_𝑖 (c) − 𝑝 ̂_(𝑖 ) (c))〗^2 
		
		
		where                                  
		 ∆_𝑖𝑗^𝑜𝑏𝑗 = 1 if an object appears in cell i, otherwise 0.
		𝑝 ̂_(𝑖 ) (c) denotes the conditional class probability for class c in cell i.

Localization Loss: The localization loss measures the errors in the predicted boundary box locations and sizes.

      λcoord ∑1_(𝑖=0)^(𝑠^2)▒∑1_(𝑗=0)^𝐵▒∆_𝑖𝑗^𝑜𝑏𝑗  [ (xi - 𝑥 ̂i)2 + (yi - 𝑦 ̂i)2 ] + λcoord ∑1_(𝑖=0)^(𝑠^2)▒∑1_(𝑗=0)^𝐵▒∆_𝑖𝑗^𝑜𝑏𝑗  [ (√(𝑤_𝑖 ) - √(𝑤 ̂_𝑖 ) )2 + (√(ℎ_𝑖 ) - √(ℎ ̂_𝑖 ) )2 ] 
      
Where

      ∆_𝑖𝑗^𝑜𝑏𝑗 = 1 if the jth boundary box in cell i is responsible for detecting the object, otherwise 0.
      
      λcoord increase the weight for the loss in the boundary box coordinates.


Confidence Loss: The confidence loss measures the accuracy of the predicted objectness score, which indicates the presence of a face in the bounding box.
∑1_(𝑖=0)^(𝑠^2)▒∑1_(𝑗=0)^𝐵▒∆_𝑖𝑗^𝑜𝑏𝑗  (𝐶_𝑖  − 𝐶 ̂_𝑖  )^2  
    

     Where
 
      ∆_𝑖𝑗^𝑜𝑏𝑗 = 1 if the jth boundary box in cell i is responsible for detecting the object, otherwise 0.
〖      𝐶 ̂〗_𝑖 is the box confidence score of the box j in cell i.


 Confidence Loss:

            If an object is not detected in the box, the confidence loss is:
𝜆_𝑛𝑜𝑜𝑏𝑗 ∑1_(𝑖=0)^(𝑠^2)▒∑1_(𝑗=0)^𝐵▒∆_𝑖𝑗^𝑛𝑜𝑜𝑏𝑗   (𝐶_𝑖  − 𝐶 ̂_𝑖  )^2
 

where
∆_𝑖𝑗^𝑛𝑜𝑜𝑏𝑗 = 1 is the complement of  ∆_𝑖𝑗^𝑜𝑏𝑗.
𝐶 ̂_𝑖 is the box confidence score of the box j in cell i.
𝜆_𝑛𝑜𝑜𝑏𝑗 weights down the loss when detecting background.
 
The final loss adds localization, confidence and classification losses together. 
     

# 5. Experimental Results:
We evaluated the performance of our face detection and recognition system on a separate test dataset. For face detection, we measured the accuracy in terms of precision, recall, and F1-score. We also conducted real-time experiments to assess the computational efficiency of our system.

## Face detection model result

![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/85369872-07f7-4bf4-b902-4aca03200dec)
![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/fff170c2-493e-442a-a0b1-36bf5f182b16)



## Face recognition model result
![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/18b6d734-215f-44f8-8480-232710e73822)
![image](https://github.com/aritra1617/Face_recongnition_model/assets/99130267/b9bba483-055a-4d2e-bfcc-1254b89ffec1)



