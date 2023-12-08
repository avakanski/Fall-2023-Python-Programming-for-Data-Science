# Import libraries
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import os
from joblib import load

# Load and split data
housing = fetch_california_housing(as_frame=True).frame
X = housing.drop('MedHouseVal', axis=1)
y = housing['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X,  y, random_state=13, test_size=0.2)

# Directory paths 
MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)

# Load model
model = load(MODEL_PATH)

# Run inference
y_pred = model.predict(X_test[:10])
print("Predicted price by the model:", np.around(y_pred,1))
np.set_printoptions(precision=1)
print("Ground-truth price:", np.array(y_test[:10]))