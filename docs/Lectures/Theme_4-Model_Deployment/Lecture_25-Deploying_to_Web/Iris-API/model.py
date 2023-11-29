# Import libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('iris.csv')

# Convert the label column into ordinal format
label_feature = data[['variety']]
label_encoder = LabelEncoder()
label_encoded = label_encoder.fit_transform(label_feature)
data['variety'] = pd.DataFrame(label_encoded, columns=label_feature.columns, index=label_feature.index)

# Extract the features X and target y variables
X = data.drop(['variety'], axis=1)
y = data['variety']

# Train a Logistic Regression model
logreg_model = LogisticRegression()
logreg_model.fit(X, y) 

# Predict the iris class based on inputs a, b, c, d
def classify(a, b, c, d):
    arr = np.array([a, b, c, d], dtype=np.float64) # Convert to numpy array
    query = arr.reshape(1, -1) # Reshape the array
    prediction = logreg_model.predict(query) # Make a prediction 
    variety = variety_mappings[prediction[0]] # Map the prediction to iris variety
    return variety # Return the iris variety

# Dictionary containing the mapping
variety_mappings = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}