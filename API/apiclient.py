import random
import requests
import numpy as np



#URL exemple 

input_features = np.random.randint(0, 1000000, size=46).tolist()

url = 'http://127.0.0.1:5000/predict'
params = {'features': input_features}

# Making a GET request with URL parameters
response = requests.get(url, params=params)

print('URL:', response.url)

