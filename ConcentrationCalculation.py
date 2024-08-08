from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import logging

""" ConcentrationCalculation.py 
Calculates the Needed values from the CSV.
"""

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ConcentrationCalculation:
    def __init__(self) -> None:
        self.__conMean = None
        self.__conStd = None
        self.__conSum = None

        # Reads in Environment Variable for CSV path
        try:
            self.__fn = os.environ.get('CON_CSV')
        except KeyError:
            logger.error("Environment Variable not found")
            raise
        try:
            self.__df_con = pd.read_csv(self.__fn)
        except FileNotFoundError:
            logger.error(f"File not found: {self.__fn}")
            raise
        except pd.errors.EmptyDataError:
            logger.error(f"No data: {self.__fn}")
            raise
        except pd.errors.ParserError:
            logger.error(f"Parsing error: {self.__fn}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

        # Segments data based on column names
        try:
            self.__df_x = self.__df_con['x']
            self.__df_y = self.__df_con['y']
            self.__df_z = self.__df_con['z']
            self.__col_con = self.__df_con['concentration']
        except KeyError as e:
            logger.error(f"Missing column in CSV: {e}")
            raise

        logger.info("Entered Constructor")
    
    # For Mean of Concentration
    def calcMean(self):
        if self.__conMean is None:
            self.__conMean = np.mean(self.__col_con)
            logger.info(self.__conMean)
        return self.__conMean

    # For Standard Deviation (Pop) of Concentration 
    def calcStdDev(self):
        if self.__conStd is None:
            self.__conStd = np.std(self.__col_con)
            logger.info(self.__conStd)
        return self.__conStd

    # For Sum of Concentration
    def calcSum(self):
        if self.__conSum is None:
            self.__conSum = np.sum(self.__col_con)
            logger.info(self.__conSum)
        return self.__conSum

    # For Image of Points using a 3D Scatter Plot w/ Concentration for Color
    def calcImg(self):
        if not (os.path.isfile('./static_images/Aeris_ScatterPlot.png')):
            fig = plt.figure(figsize = (10,10))
            ax = plt.axes(111, projection='3d')
            sctt = ax.scatter3D(self.__df_x, self.__df_y, self.__df_z, c = self.__col_con, s = 50)
            plt.title("Aeris Scatter Plot")
            ax.set_xlabel('X-axis', fontweight ='bold') 
            ax.set_ylabel('Y-axis', fontweight ='bold') 
            ax.set_zlabel('Z-axis', fontweight ='bold')
            cbar = fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
            cbar.ax.set_ylabel('Concentration', rotation=270, labelpad=10)
            logger.info(self.__col_con.max())

            #Saves Images for Controller
            plt.savefig('./static_images/Aeris_ScatterPlot.png')

        #Returns Absolute Path for Controller
        return os.path.abspath('./static_images/Aeris_ScatterPlot.png')


