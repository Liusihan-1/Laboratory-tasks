import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

data_train = pd.read_csv('train.csv')
Survived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
Survived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
df = pd.DataFrame({u'live': Survived_1, u'unlive': Survived_0})
df.plot(kind='bar', stacked=True)
plt.show()
