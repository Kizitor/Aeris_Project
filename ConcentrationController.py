from flask import Flask, send_file, jsonify
import ConcentrationCalculation

""" ConcentrationController.py 
Manages and Publishes REST API Endpoints for Use
"""

# Creates App with Classname
app = Flask(__name__)

CC = ConcentrationCalculation.ConcentrationCalculation()

# Returns JSON of Mean Value
@app.get('/get-mean')
def get_mean():
    return jsonify({'mean': CC.calcMean()})

# Returns JSON of Standard Deviation Value
@app.get('/get-std-deviation')
def get_std_deviation():
    return jsonify({'standard_deviation': CC.calcStdDev()})

# Returns JSON of Sum Value
@app.get('/get-sum')
def get_sum():
    return jsonify({'sum': CC.calcStdDev()})

# Returns a PNG of Concentration
@app.get('/get-image')
def get_image():
    return send_file(CC.calcImg(), mimetype='image/png')