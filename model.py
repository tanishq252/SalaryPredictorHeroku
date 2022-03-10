import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


dataSet = pd.read_csv("Position_Salaries.csv")

def model(salary):
    x = dataSet.iloc[:,1:-1].values
    y = dataSet.iloc[:,-1].values

    # more the number of n_estimators better the accuracy
    # more time complexity tho :p
    RFModel = RandomForestRegressor(n_estimators=11)
    RFModel.fit(x,y)
    RFModel.score(x,y)

    salary = np.array(salary).reshape(-1,1)
    answer  = (RFModel.predict(salary))

    return answer

out = model(12)
print(out)