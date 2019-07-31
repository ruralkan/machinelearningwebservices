
The goal is make a Machine learning Web service that can predict on images of handwritten digits, we can extended to facial recognition or identify fraudulent checks.
We are using a [Python Web Framework](https://hackernoon.com/top-10-python-web-frameworks-to-learn-in-2018-b2ebab969d1a) named [Tornado](https://www.tornadoweb.org/en/stable/), a Python web framework and asynchronous networking library.

## Objetives

- Create an endpoint/ predict, which take s in one parameter "input"
- Will store entire vector of data at this argument.
- App will make prediction using model, return JSON with prediction {"prediction": k}
- Make it a POST even though POST's technically should be used for requests which change data on server.
- Don't want entire vector to show up in URL (would happen with GET)

## Instructions
- First, run in terminal `python app_trainer.py` to train the Random Forest Classifier model and save the trained model (mymodel.pkl)
- After that, open two terminals (t1, t2), in t1 run `python3 app.py`to start the server
- In t2 run `python3 app_caller.py` to run the service caller



