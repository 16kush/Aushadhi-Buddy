# Aushadhi Buddy - Medical Chatbot

Aushadhi Buddy is an intelligent and interactive medical chatbot designed to help users identify symptoms and provide predictions on potential health conditions based on the information provided. The chatbot utilizes advanced machine learning algorithms to offer accurate predictions and medical advice to users, making healthcare information more accessible and user-friendly.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)

## Requirements

Python 3.5 or newer.

Dependencies:

- Flask
- PyTorch
- NLTK
- NumPy
- Scikit-learn
- Pandas
- matplotlib

## Install requirements

Before running the application you need to install the dependencies. We recommend to use the virtual environment
[virtualenv](https://pypi.org/project/virtualenv/) for this.

Windows:

```
py -3 -m venv venv
venv\Scripts\activate
pip install flask torch nltk numpy==1.19.3 sklearn pandas matplotlib
```



In order for _nltk_ tokenization to work, the _'punkt'_ package must be downloaded. To do this, simply enter the Python shell and run the following:

```python
import nltk
nltk.download('punkt')
```

This will install all the required dependencies needed to run the application successfully.

## Run

1. To run MedicalChatbot, `cd` into MedicalChatbot repo on your computer and run `python -m flask run`. This will run the Flask 
server in development mode on localhost, port 5000.

`* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`



## Features

- **User-friendly Interface**: Aushadhi Buddy offers an intuitive and easy-to-use interface for users to describe their symptoms.

- **Symptom Analysis**: The chatbot uses advanced natural language processing techniques to analyze and understand the symptoms provided by users.

- **Accurate Predictions**: Utilizing PyTorch, the chatbot provides accurate predictions and potential health conditions based on the user's symptoms.

- **Medical Advice and Suggestions**: Aushadhi Buddy offers helpful medical advice and suggestions to users based on their symptoms.

- **Interactive Chat Experience**: The chatbot engages users in an interactive and human-like conversation for a personalized experience.


## Technologies-Used

- **Flask**: A micro web framework used to build the backend server. [Learn More](https://flask.palletsprojects.com/)

- **PyTorch**: A powerful open-source machine learning library used for implementing the chatbot's prediction model. [Learn More](https://pytorch.org/)

- **NLTK**: The Natural Language Toolkit, used for text processing and tokenization in the chatbot. [Learn More](https://www.nltk.org/)

- **NumPy**: A fundamental package for scientific computing with Python, used for data manipulation. [Learn More](https://numpy.org/)

- **Scikit-learn**: A popular machine learning library used for data mining and data analysis. [Learn More](https://scikit-learn.org/)

- **Pandas**: A versatile data manipulation library for Python, used for data analysis. [Learn More](https://pandas.pydata.org/)

- **matplotlib**: A data visualization library used for creating charts and plots. [Learn More](https://matplotlib.org/)

## Demo Video

<video width="640" height="360" controls>
  <source src="https://github.com/16kush/Aushadhi-Buddy/raw/main/static/Demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

