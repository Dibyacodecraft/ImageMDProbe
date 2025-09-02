from flask import Flask, request, jsonify, send_from_directory
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image
from io import BytesIO

app = Flask(__name__, static_folder='static')

# Load your trained model
model = tf.keras.models.load_model('D:/Sanjib Sahu/Image MD Probe/model/skin_disease_model.h5')

# Assuming you have a list of class names corresponding to your model's output classes
class_names = ['AcnePittedScars', 'PerioralDerm1', 'PerioralDermEye', 'PerioralSteroid', 'PerlecheAccutane', 'Rhinophyma', 'SteroidPerioral', 'VascularFace0120', 'VesselsNose', 'acne-Closed-Comedo', 'acne-cystic', 'acne-excoriated', 'acne-histology', 'acne-infantile', 'acne-open-comedo', 'acne-pustular', 'acne-scar', 'rosacea010206OK', 'sebDerem110105']

def predict_disease(img):
    try:
        img = Image.open(img)
        img = img.resize((150,150)) 
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        predicted_class_index = np.argmax(prediction)

        predicted_class_name = class_names[predicted_class_index]
        return predicted_class_name

    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})

        img = request.files['image']
        predicted_disease = predict_disease(img)

        return jsonify({'diagnosis': predicted_disease})

    except Exception as e:
        return jsonify({'error': str(e)})

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'templets'), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
