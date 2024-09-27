# Streamlit-Base-App

To start with this project we need to create a virtual environment for python.
To do that open cmd and run

```console
conda create -p venv python==3.12 -y 
conda activate venv
conda install pip
```

Next we need to install all the required packages.
Create a requirements.txt file and list all the packages that we will need there.
Then run this code in cmd

```console
pip install -r requirements.txt
```

Now the environment is ready so the process of building the app can start.

## How to build the Streamlit App

Step 1. Create the app.py script which will be used to create the App.
Step 2. Create the notebook where you can test your code step by step.

To be able and run your app, you have to run the below code in cmd

```console
streamlit run app.py
```

Similarly you can create other apps with widgets or even an ML model