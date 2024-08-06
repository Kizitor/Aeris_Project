import pytest
import sys
sys.path.append('../')
import ConcentrationCalculation
import os


os.environ['CON_CSV'] = os.path.abspath('./test_con.csv')
CC = ConcentrationCalculation.ConcentrationCalculation()

def test_mean():
    assert CC.calcMean() == 1.5

def test_stdDev():
    assert CC.calcStdDev() == 0

def test_sum():
    assert CC.calcSum() == 4.5

def test_img():
    print(os.path.isfile(CC.calcImg()))

