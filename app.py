from flask import Flask, request, jsonify, render_template
import cv2
import base64  # Import base64 for image encoding

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
  data = request.get_json()
  image_data = data['image'].split(',')[1]  # Extract base64 data

  # Decode base64 string and convert to byte array
  image_bytes = bytes(image_data, 'utf-8')
  decoded_image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

  # Process the image using OpenCV
  # (Replace this with your desired OpenCV processing logic)
  gray_image = cv2.cvtColor(decoded_image, cv2.COLOR_BGR2GRAY)

  # Send processed image information back to the browser (optional)
  return jsonify({'grayscale': True})  # Example response

if __name__ == '__main__':
    app.run(debug=True)
