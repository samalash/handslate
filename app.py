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

@app.route('/process_image', methods=['POST'])
def process_image():
  data = request.get_json()
  image_data = data['frame'].split(',')[1]  # Extract base64 data

    # Decode base64 strin and convert to byte array
  image_bytes = base64.b64decode(image_data)
  nparr = np.frombuffer(image_bytes, np.uint8)
  decoded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
  print(type(decoded_image))

  #print(image_bytes)
  #decoded_image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

    # Process the image using OpenCV
    # (Replace this with your desired OpenCV processing logic)
    
  filename = '{}.jpg'.format(uuid.uuid1())
  cv2.imwrite(os.path.join('assets/Output Images', filename), decoded_image)

  preprocessed_image = preprocess_image(filename)
  predictions = model.predict(preprocessed_image)
  predicted_class = np.argmax(predictions, axis=1)
  print("Predicted class:", predicted_class)
  print("Predicted letter:", classToLetter(predicted_class[0]))

    # Send processed image information back to the browser (optional)
  return jsonify({'message': "Image captured"})  # Example response
  #except:
     #print("Here")
     #return jsonify({'message': "Error 415 happened again"})
  

if __name__ == '__main__':
    app.run(debug=True)
