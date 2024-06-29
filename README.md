# Cifar_vgg16

This project demonstrates how to perform image classification on the CIFAR-10 dataset using a VGG16 convolutional neural network. The model is implemented using TensorFlow and Keras, and the application is built as a Flask API, which can be containerized using Docker.

Prerequisites
Python 3.10+
pip (Python package installer)
Virtualenv (optional but recommended)
Docker (optional, for containerization)

Clone repo
git clone https://github.com/shelearnai/Cifar_vgg16.git
cd Cifar_vgg16

Setup env
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies
pip install -r requirements.txt

Run the flask apps
python app.py


Certainly! Here's a README file for the repository located at https://github.com/shelearnai/Cifar_vgg16:

CIFAR-10 Image Classification with VGG16
This project demonstrates how to perform image classification on the CIFAR-10 dataset using a VGG16 convolutional neural network. The model is implemented using TensorFlow and Keras, and the application is built as a Flask API, which can be containerized using Docker.

Table of Contents
Introduction
Installation
Usage
API Endpoints
Docker
Contributing
License
Introduction
The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class. This project uses the VGG16 architecture, pretrained on ImageNet, to classify these images into one of the following classes:

Airplane
Automobile
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck
The trained model is exposed as a RESTful API using Flask, allowing users to upload an image and receive a prediction of its class.

Installation
Prerequisites
Python 3.7+
pip (Python package installer)
Virtualenv (optional but recommended)
Docker (optional, for containerization)
Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/shelearnai/Cifar_vgg16.git
cd Cifar_vgg16
Set Up the Environment
It's recommended to use a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Download Pretrained Model
Download the pretrained VGG16 model weights (cifar10_vgg16.h5) from the release page and place it in the project directory.

Usage
Run the Flask Application
Start the Flask application:

bash
Copy code
python app.py
The application will be accessible at http://localhost:5000.

Test the API with Postman
Open Postman.
Create a new POST request to http://localhost:5000/predict.
Select the form-data option under the Body tab.
Add a key named file with type File and choose an image file to upload.
Send the request and check the response for the predicted class.

Docker
Build and Run with Docker
docker build -t cifar-vgg16 .
docker run -p 5000:5000 cifar-vgg16




