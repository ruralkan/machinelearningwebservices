# Trains model on data and save it
# Model random forest classifier
# The pickle module implements binary protocols for serializing
# and de-serializing a Python object structure.

import pickle
import numpy as np
from util import get_data
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
    X, Y = get_data()
    Ntrain = len(Y) // 4
    Xtrain, Ytrain = X[:Ntrain], Y[:Ntrain]

    model = RandomForestClassifier()
    model.fit(Xtrain, Ytrain)

    # just in case you're curious
    Xtest, Ytest = X[Ntrain:], Y[Ntrain:]
    print("test accuracy:", model.score(Xtest, Ytest))

    with open('mymodel.pkl', 'wb') as f:
        pickle.dump(model, f)