import numpy as np
import cv2

# Define the paths to the video and the model
video_path = 'Video Detection/video.mp4'
prototxt_path = 'MobileNetSSD_deploy.prototxt'
model_path = 'MobileNetSSD_deploy.caffemodel'
min_confidence = 0.5

# Define the class labels
classes = ['background', 
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor']

# Generate random colors for each class
np.random.seed(543210)
colors = np.random.uniform(0, 255, size=(len(classes), 3)).astype(int)

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Load the video
cap = cv2.VideoCapture(video_path)

# Get the video frame rate and size
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30.0  # Default frame rate

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output2.avi', fourcc, fps, (frame_width, frame_height))

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Create a blob from the frame
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    
    # Set the input for the model
    net.setInput(blob)
    
    # Run the object detection
    detected_objects = net.forward()
    
    # Loop through the detected objects
    for i in range(detected_objects.shape[2]):
        confidence = detected_objects[0][0][i][2]
        if confidence > min_confidence:
            class_index = int(detected_objects[0, 0, i, 1])
            if class_index < len(classes):
                upper_left_x = int(detected_objects[0, 0, i, 3] * frame.shape[1])
                upper_left_y = int(detected_objects[0, 0, i, 4] * frame.shape[0])
                lower_right_x = int(detected_objects[0, 0, i, 5] * frame.shape[1])
                lower_right_y = int(detected_objects[0, 0, i, 6] * frame.shape[0])
                
                # Draw a rectangle around the detected object
                cv2.rectangle(frame, 
                              (upper_left_x, upper_left_y), 
                              (lower_right_x, lower_right_y), 
                              tuple(map(int, colors[class_index])), 
                              2)
                
                # Create a text label for the detected object
                prediction_text = f"{classes[class_index]}: {confidence:.2f}"
                
                # Draw the text label above the rectangle
                cv2.putText(frame, 
                            prediction_text, 
                            (upper_left_x, upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.6, 
                            tuple(map(int, colors[class_index])), 
                            2)
    
    # Write the frame to the output video
    out.write(frame)

# Release the video capture and close the output video
cap.release()
out.release()
cv2.destroyAllWindows()
