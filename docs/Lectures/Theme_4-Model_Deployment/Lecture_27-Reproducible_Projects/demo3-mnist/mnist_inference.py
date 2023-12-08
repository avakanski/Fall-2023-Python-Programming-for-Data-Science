# Import modules
import numpy as np
import tensorflow
import tensorflow.keras as keras
from keras.models import load_model

# Load the dataset
mnist_fashion = keras.datasets.fashion_mnist
(training_images, training_labels), (test_images,test_labels) = mnist_fashion.load_data()

# Scaling 
test_images = test_images/255.0

# loading the weights
cnn_model = load_model("cnn_model.keras")

# Predict
print("Predict the digit in the first 10 images in the test dataset")
y_pred = cnn_model.predict(test_images[:10])
print("Predicted image label:", np.argmax(y_pred,1))
print("Ground-truth image label:", test_labels[:10])
