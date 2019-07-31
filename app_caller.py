## To simulate how an external app would call web service (API)
## We can choose digit at random
## Call the web service to make prediction and print prediction
## + True label, show image

import requests
import numpy as np
import matplotlib.pyplot as plt
from util import get_data

# make a prediction from our own server!
# in reality this could be coming from any client

X, Y = get_data()
N = len(Y)
while True:
    i = np.random.choice(N)
    r = requests.post("http://localhost:8888/predict", data={'input': X[i]})
    print("RESPONSE:")
    print(r.content)
    j = r.json()
    print(j)
    print("target:", Y[i])

    plt.imshow(X[i].reshape(28, 28), cmap='gray')
    plt.title("Target: %d, Prediction: %d" % (Y[i], j['prediction']))
    plt.show()

    response = input("Continue? (Y/n)\n")
    if response in ('n', 'N'):
        break