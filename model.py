import cv2
import os
import uuid
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

def classToLetter(classnum):
    #converts class number to corresponding letter (0-28 -> A-Z, del, nothing, space)
    if classnum == 26:
        return "del"
    if classnum == 27:
        return "nothing"
    if classnum == 28:
        return "space"
    return chr(classnum + 65)
    


# Load the model from the .h5 file
model = load_model('models/asl_vgg16_best_weights.h5')

# Define a function to preprocess input images
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(64, 64))  # Adjust target size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Example usage: Make predictions on a new image
new_image_path = 'assets/Test Images/A.jpeg'
preprocessed_image = preprocess_image(new_image_path)
predictions = model.predict(preprocessed_image)

# Assuming your model has multiple classes and you want the class with the highest probability
predicted_class = np.argmax(predictions, axis=1)
print("Predicted class:", predicted_class)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pic = cv2.cvtColor(pic, cv2.COLOR_RGB2BGR)


    if cv2.waitKey(10) & 0xFF == ord('p'):
         print("make sure")
         cv2.imwrite(os.path.join('assets/Output Images', '{}.jpg'.format(uuid.uuid1())), pic)


    cv2.imshow('Hand Tracking', pic)

    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
