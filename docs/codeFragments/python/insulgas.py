#import numpy as np

import pandas as pd
import codecs
import io
import requests

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

DATA_PATH = Path.cwd()


url = "https://raw.githubusercontent.com/EnvironmentalStatistics/prepareData/refs/heads/main/data/insulgas/insulgas.csv"
stream=requests.get(url).content
dataframe=pd.read_csv(io.StringIO(stream.decode('utf-8')), delimiter=',')
print(dataframe)

'''
from csvw import CSVW
csvw = "https://raw.githubusercontent.com/EnvironmentalStatistics/prepareData/refs/heads/main/data/insulgas/insulgas.json"
dataframe = CSVW(csvw)
print(dataframe)
'''

sns.set_theme(style="ticks")
f, ax = plt.subplots(figsize=(9, 9))
sns.scatterplot(x="Gas", y="Temp", hue="Insulate", data=dataframe)
f.savefig(DATA_PATH / 'insulgas.png', dpi=300)





