import cv2
import os

# Set the video path and output directory
video_path = os.getcwd()+"\\..\\"+"te6.mp4"
output_dir = os.getcwd()+"\\..\\video_pics"

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get the total number of frames and frame rate
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Loop through the video and extract frames
# Set the frame rate to extract one frame per second
frame_rate = 1
frame_interval = int(round(fps / frame_rate))

frame_count = 0
while True:
    # Read the current frame
    ret, frame = cap.read()
    if not ret:
        break

    # Extract one frame per second
    if frame_count % frame_interval == 0:
        # Save the frame as an image file
        frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)

    frame_count += 1

    # Stop if the number of extracted frames reaches the total number of frames
    if frame_count >= total_frames:
        break

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()

pathname=os.getcwd()+"\\..\\test.txt"
with open(pathname,'w') as f:
    for file in os.listdir(output_dir):
        name = f'video_pics/{file}'+"\n"
        f.write(name)
    f.close()
