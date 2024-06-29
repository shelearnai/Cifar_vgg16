from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = load_model('cifar10_vgg16.h5')

# CIFAR-10 class labels
cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

@app.route('/')
def home():
    return "Welcome to the CIFAR-10 Image Classification API!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    img = Image.open(file.stream)  # Open image using PIL
    img = img.resize((32, 32))  # Resize image to match model input size
    img_array = np.array(img) / 255.0  # Convert image to array and normalize

    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction[0])
    class_name = cifar10_classes[class_idx]

    return jsonify({'class_name': class_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
