import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

df = pd.read_csv("./cars.csv")


# pre-processing
df["speed"] = df["speed"] * 1.60934  # mph to kmh
df["dist"] = df["dist"] * 0.3048  # ft to meters


# plot the data
plt.scatter(df["speed"], df["dist"])
plt.xlabel("Speed")
plt.ylabel("Distance")
plt.savefig("cars_scatter.png")


# model using linear regression
X = df["speed"].to_numpy().reshape(-1, 1)
Y = df["dist"].to_numpy()
reg = linear_model.LinearRegression()
reg.fit(X, Y)
print("Coefficients: \n", reg.coef_)

predicted_Y = reg.predict(X)

plt.plot(X, predicted_Y, color="red")
plt.savefig("cars_regression.png")

X = sm.add_constant(X) # add const to allow for constant offset of gradient
stats_results = sm.OLS(Y, X).fit()
print(stats_results.summary())
