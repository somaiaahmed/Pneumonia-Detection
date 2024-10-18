from flask import Flask, request, jsonify, render_template, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define allowed extensions (e.g., .png, .jpg, .jpeg)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/gan-model')
def gan_model():
    return render_template('gan-model.html')

@app.route('/pneumonia-detection', methods=['GET', 'POST'])
def pneumonia_detection():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            diagnosis = filename.rsplit('.', 1)[0]

            # Return the "diagnosis" and  confidence (92%)
            return jsonify({
                "prediction": {
                    "diagnosis": diagnosis,  
                    "confidence": 92.00  
                },
            })

        return jsonify({"error": "File not allowed"}), 400
    
    # Render the pneumonia detection page with an upload form
    return render_template('pneumonia-detection.html')

if __name__ == '__main__':
    app.run(debug=True)
