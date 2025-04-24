import numpy as np
import cv2
import matplotlib.pyplot as plt

# Define the paths to the image and the model
image_path = "Image Detection\Capture(1).PNG"
prototxt_path = 'MobileNetSSD_deploy.prototxt'
model_path = 'MobileNetSSD_deploy.caffemodel'
min_confidence = 0.01

# Define the class labels
classes = ['background', 
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor']

# Generate random colors for each class
np.random.seed(543210)
colors = np.random.uniform(0, 255, size = (len(classes), 3)).astype(int)

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Load the image
image = cv2.imread(image_path)

# Create a blob from the image
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

# Set the input for the model
net.setInput(blob)

# Run the object detection
detected_objects = net.forward()

# Loop through the detected objects
for i in range(detected_objects.shape[2]):
    confidence = detected_objects[0][0][i][2]
    if confidence > min_confidence:
        class_index = int(detected_objects[0, 0, i, 1])
        upper_left_x = int(detected_objects[0, 0, i, 3]*image.shape[1])
        upper_left_y = int(detected_objects[0, 0, i, 4]*image.shape[0])
        lower_right_x = int(detected_objects[0, 0, i, 5]*image.shape[1])
        lower_right_y = int(detected_objects[0, 0, i, 6]*image.shape[0])

        # Draw a rectangle around the detected object
        image = cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), tuple(map(int, colors[class_index])), 2)

        # Create a text label for the detected object
        prediction_test = f"{classes[class_index]}: {confidence:.2f}%"

        # Draw the text label above the rectangle
        cv2.putText(image, prediction_test, (upper_left_x, upper_left_y - 15 if upper_left_y > 30 else upper_left_y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, tuple(map(int, colors[class_index])), 2)

# Display the output using matplotlib
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()