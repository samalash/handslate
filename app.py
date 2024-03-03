from flask import Flask, request, jsonify, render_template
import cv2
import base64  # Import base64 for image encoding
import numpy as np
from model import classToLetter, preprocess_image, model
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST']) #Connected to the Fetch
def process_image():
  data = request.get_json() #Gets the data from the frontend
  image_data = data['frame'].split(',')[1]  # Extract base64 data

  # Decode base64 strin and convert to byte array
  image_bytes = base64.b64decode(image_data)
  nparr = np.frombuffer(image_bytes, np.uint8)
  decoded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR) #this is now the image file itself
    
  #Create a file in Output Images of this image
  filename = '{}.jpg'.format(uuid.uuid1()) 
  cv2.imwrite(os.path.join('assets/Output Images', filename), decoded_image)
  filename = os.path.join('assets/Output Images', filename)

  #Use the filepath of the newly created image to run through the model
  preprocessed_image = preprocess_image(filename)
  predictions = model.predict(preprocessed_image)
  predicted_class = np.argmax(predictions, axis=1)
  print("Predicted class:", predicted_class) 
  print("Predicted letter:", classToLetter(predicted_class[0]))
  os.remove(filename) #Delete the file afterwards

  return jsonify({'message': "Image captured"}) 

  #except:
     #print("Here")
     #return jsonify({'message': "Error 415 happened again"})
  

if __name__ == '__main__':
    app.run(debug=True)
