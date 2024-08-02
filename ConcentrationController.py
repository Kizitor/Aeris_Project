from flask import Flask

app = Flask(__name__)

@app.get('/get-mean')
def get_mean():
    pass

@app.get('/get-std-deviation')
def get_std_deviation():
    pass

@app.get('/get-sum')
def get_sum():
    pass

@app.get('/get-image')
def get_image():
    pass