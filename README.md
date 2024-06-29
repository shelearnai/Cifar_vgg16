# Cifar_vgg16

This project demonstrates how to perform image classification on the CIFAR-10 dataset using a VGG16 convolutional neural network. The model is implemented using TensorFlow and Keras, and the application is built as a Flask API, which can be containerized using Docker.
<br>
Prerequisites
Python 3.10+
pip (Python package installer)
Virtualenv (optional but recommended)
Docker (optional, for containerization)
<br>
Clone repo
git clone https://github.com/shelearnai/Cifar_vgg16.git
cd Cifar_vgg16

<br>
Setup env
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
<br>
Install dependencies
pip install -r requirements.txt
<br>
Run the flask apps
python app.py

The application will be accessible at http://localhost:5000.

<br>
Test the API with Postman
Open Postman.
Create a new POST request to http://localhost:5000/predict.
Select the form-data option under the Body tab.
Add a key named file with type File and choose an image file to upload.
Send the request and check the response for the predicted class.
<br>
Docker
Build and Run with Docker
docker build -t cifar-vgg16 .
docker run -p 5000:5000 cifar-vgg16




