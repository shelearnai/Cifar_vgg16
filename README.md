# Cifar_vgg16
<br>
This project demonstrates how to perform image classification on the CIFAR-10 dataset using a VGG16 convolutional neural network. The model is implemented using TensorFlow and Keras, and the application is built as a Flask API, which can be containerized using Docker.
<br>
## Prerequisites<br>
Python 3.10+<br>
pip (Python package installer)<br>
Virtualenv (optional but recommended)<br>
Docker (optional, for containerization)<br>
<br><br><br>
### Clone repo
git clone https://github.com/shelearnai/Cifar_vgg16.git<br>
cd Cifar_vgg16<br>

<br>
###Setup env<br>
python -m venv venv<br>
source venv/bin/activate  # On Windows use `venv\Scripts\activate`<br>
<br>
### Install dependencies<br>
pip install -r requirements.txt<br>
<br><br><br>
### Run the flask apps<br>
python app.py<br>
The application will be accessible at http://localhost:5000.<br>

<br>
### Test the API with Postman<br>
Open Postman.<br>
Create a new POST request to http://localhost:5000/predict.<br>
Select the form-data option under the Body tab.<br>
Add a key named file with type File and choose an image file to upload.<br>
Send the request and check the response for the predicted class.<br>
<br>
### Docker<br>
Build and Run with Docker<br>
docker build -t cifar-vgg16 .<br>
docker run -p 5000:5000 cifar-vgg16<br>


![image](https://github.com/shelearnai/Cifar_vgg16/assets/6790548/d24a2740-6d52-4ba6-94c3-bfcce650be0a)


