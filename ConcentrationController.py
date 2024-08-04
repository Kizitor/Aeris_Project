from flask import Flask, send_file, jsonify
import ConcentrationCalculation

app = Flask(__name__)
CC = ConcentrationCalculation.ConcentrationCalculation()

@app.get('/get-mean')
def get_mean():
    return jsonify({'mean': CC.calcMean()})

@app.get('/get-std-deviation')
def get_std_deviation():
    return jsonify({'standard_deviation': CC.calcStdDev()})

@app.get('/get-sum')
def get_sum():
    return jsonify({'sum': CC.calcStdDev()})

@app.get('/get-image')
def get_image():
    return send_file(CC.calcImg(), mimetype='image/png')