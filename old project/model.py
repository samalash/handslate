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
# Make sure to download the newest model from github!!!!!!
model = load_model('models/asl_vgg16_newer_weights.h5')

# Define a function to preprocess input images
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))  # Adjust target size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# Below is our original implrementation. This python code pulled up the webcam
# and when certain keys were pressed, saved the frame and ran it through the model
# to output a result (predict the letter)
'''
# Example usage: Make predictions on a new image
new_image_path = 'assets/Test Images/A.jpeg'
preprocessed_image = preprocess_image(new_image_path)
predictions = model.predict(preprocessed_image)

# Assuming your model has multiple classes and you want the class with the highest probability
predicted_class = np.argmax(predictions, axis=1)
print("Predicted class:", predicted_class)

cap = cv2.VideoCapture(0) #Opens the webcam from the comptuer
while cap.isOpened(): 
    ret, frame = cap.read() #Reads the frame from the webcam

    if cv2.waitKey(10) & 0xFF == ord('p'):
         # press p to take a picture and have the network predict letter
         
         print("make sure")
         filename = '{}.jpg'.format(uuid.uuid1())
         cv2.imwrite(os.path.join('assets/Output Images', filename), frame)
         filename = os.path.join('assets/Output Images', filename)
         print(filename)
         preprocessed_image = preprocess_image(filename)
         predictions = model.predict(preprocessed_image)
         predicted_class = np.argmax(predictions, axis=1)
         print("Predicted class:", predicted_class)
         print("Predicted letter:", classToLetter(predicted_class[0]))
         os.remove(filename)


    if cv2.waitKey(10) & 0xFF == ord('s'):
         # press s to take a picture and save, to have the network predict letter

         print("make sure")
         filename = '{}.jpg'.format(uuid.uuid1())
         cv2.imwrite(os.path.join('assets/Output Images', filename), frame)
         filename = os.path.join('assets/Output Images', filename)
         print(filename)
         preprocessed_image = preprocess_image(filename)
         predictions = model.predict(preprocessed_image)
         predicted_class = np.argmax(predictions, axis=1)
         print("Predicted class:", predicted_class)
         print("Predicted letter:", classToLetter(predicted_class[0]))
     

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
            # press q to quit the program
            break
cap.release()
cv2.destroyAllWindows()'''
