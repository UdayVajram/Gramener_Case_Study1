import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

studData = pd.read_csv('nas-pupil-marks.csv')

boyData = studData[studData['Gender'] == 1].groupby('State').agg(
    {'Maths %': np.mean, 'Science %': np.mean, 'Reading %': np.mean, 'Social %': np.mean})
girlData = studData[studData['Gender'] == 2].groupby('State').agg(
    {'Maths %': np.mean, 'Science %': np.mean, 'Reading %': np.mean, 'Social %': np.mean})

q2 = boyData - girlData
studData['State'] = studData['State'].astype(str)

southStates = studData[
    (studData['State'] == 'AP') | (studData['State'] == 'TN') | (studData['State'] == 'KA') | (studData['State'] == 'KL')
    | (studData['State'] == 'PY') | (studData['State'] == 'LD') | (studData['State'] == 'AN')]

northStates = studData[
    (studData['State'] != 'AP') | (studData['State'] != 'TN') | (studData['State'] != 'KA') | (studData['State'] != 'KL')
    | (studData['State'] != 'PY') | (studData['State'] != 'LD') | (studData['State'] != 'AN')]


southavg = southStates.agg({'Maths %': np.mean, 'Science %': np.mean})
northavg = northStates.agg({'Maths %': np.mean, 'Science %': np.mean})

q3 = southavg - northavg

q2.plot.bar()
plt.show()

q3.plot.bar()
plt.show()
