import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the model from the .h5 file
model = load_model('models/asl_vgg16_best_weights.h5')

# Define a function to preprocess input images
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(64, 64))  # Adjust target size as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Example usage: Make predictions on a new image
new_image_path = 'assets/A.jpeg'
preprocessed_image = preprocess_image(new_image_path)
predictions = model.predict(preprocessed_image)

# Assuming your model has multiple classes and you want the class with the highest probability
predicted_class = np.argmax(predictions, axis=1)
print("Predicted class:", predicted_class)
