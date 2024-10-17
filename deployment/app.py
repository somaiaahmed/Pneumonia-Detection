from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
#from tensorflow.keras.models import load_model  # Import the correct load function


app = Flask(__name__)

"""# Load your Keras model
try:
    model = load_model('model/detection_model.h5')
except FileNotFoundError:
    print("Model file not found. Please check the path.")
    raise
except ImportError as e:
    print(f"Import error: {e}. Ensure TensorFlow and Keras are installed.")
    raise
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    raise"""

# Folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'  # Updated to include 'static/' for serving files
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define allowed extensions (e.g., .png, .jpg, .jpeg)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(filepath):
    # Load the image
    image = cv2.imread(filepath)

    # Resize the image to match the input size of the model
    # Assuming your model expects 224x224 images (modify if needed)
    image = cv2.resize(image, (224, 224))

    # Convert the image to a float32 numpy array and normalize
    image = image.astype('float32') / 255.0

    # Add a batch dimension (1, 224, 224, 3)
    image = np.expand_dims(image, axis=0)

    return image

# Route to show the main page (informative page about pneumonia)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/gan-model')
def gan_model():
    return render_template('gan-model.html')

# Route for Pneumonia Detection page
@app.route('/pneumonia-detection', methods=['GET', 'POST'])
def pneumonia_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        """if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocess the image for prediction
            image = preprocess_image(filepath)

            # Make a prediction using the loaded model
            prediction = model.predict(image)

            # Assuming the model outputs probabilities for classes [No Pneumonia, Pneumonia]
            # Modify according to your model's output
            pneumonia_probability = prediction[0][1]  # Adjust index based on your model's output shape
            diagnosis = "Pneumonia" if pneumonia_probability > 0.5 else "No Pneumonia"
            confidence = pneumonia_probability * 100  # Convert to percentage

            # Render the detection result along with the uploaded image
            return jsonify({
                "prediction": {
                    "diagnosis": diagnosis,
                    "confidence": f"{confidence:.2f}%"
                },
                "uploaded_image": url_for('static', filename='uploads/' + filename)
            })"""

        return jsonify({"error": "File not allowed"}), 400
    
    # Render the pneumonia detection page with an upload form
    return render_template('pneumonia-detection.html')

if __name__ == '__main__':
    app.run(debug=True)
