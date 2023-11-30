from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import re
import base64

# Initialize the flask class and specify the templates directory
app = Flask(__name__, template_folder="templates")

# Default route set as 'index'
@app.route('/')
def index_view():
    return render_template('index.html')

# load the saved model
model = load_model("mnist_model.keras")
# Compile the loaded model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Convert the image into a png file
def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)',imgData1).group(1)
    with open('output.png','wb') as output:
        output.write(base64.b64decode(imgstr))

# Route 'predict' 
@app.route('/predict', methods=['GET', 'POST'])
def predict_class():
    
    # Get the drawn image
    imgData = request.get_data()
    
    # Convert the image into a png file
    convertImage(imgData)

    # Open the png file    
    x = Image.open('output.png')

    # Resize the image to 28x28 pixels      
    x = x.resize((28,28))

    # Invert the image into black background and white foreground    
    x = np.invert(x)

    # Reshape into a batch with one image    
    x = x[:,:,0].reshape(1, 28, 28, 1)
    
    # Scale to the range [0,1]
    x = x/255
    
    # Make a prediction
    out = model.predict(x)
    
    # Get the predicted digit
    response = np.array_str(np.argmax(out, axis=1))
    
    return response	

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
