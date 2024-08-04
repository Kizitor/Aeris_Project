from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import numpy as np
import os
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ConcentrationCalculation:
    def __init__(self) -> None:
        self._fn = os.environ.get('CON_CSV')
        self._df_con = pd.read_csv(self._fn)
        self._df_x = self._df_con['x']
        self._df_y = self._df_con['y']
        self._df_z = self._df_con['z']
        self._col_con = self._df_con['concentration']
        logger.info("Entered Constructor")
    
    def calcMean(self):
        _conMean = np.mean(self._col_con)
        logger.info(_conMean)
        return _conMean

    def calcStdDev(self):
        _conStd = np.std(self._col_con)
        logger.info(_conStd)
        return _conStd

    def calcSum(self):
        _conSum = np.sum(self._col_con)
        logger.info(_conSum)
        return _conSum

    def calcImg(self):
        fig = plt.figure(figsize = (10,10))
        ax = plt.axes(111, projection='3d')
        sctt = ax.scatter3D(self._df_x, self._df_y, self._df_z, c = self._col_con, s = 50)
        plt.title("Aeris Scatter Plot")
        ax.set_xlabel('X-axis', fontweight ='bold') 
        ax.set_ylabel('Y-axis', fontweight ='bold') 
        ax.set_zlabel('Z-axis', fontweight ='bold')
        fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
        logger.info(self._col_con.max())
        plt.savefig('./static_images/Aeris_ScatterPlot.png')
        return os.path.abspath('./static_images/Aeris_ScatterPlot.png')


