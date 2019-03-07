import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib qt

# Import data
data = pd.read_csv("markdata.csv")

# Set date column as index of data frame
data = data.set_index("Date")

# Price data to return data
returns = data.pct_change() #arithmetic returns
logreturns = np.log(1 + returns) #log returns

logreturns.iloc[0] = 0 #first row of log returns = 0 

# Empty lists to store returns, volatility and weights of imaginary portfolios
port_returns = []
port_risk = []
port_weights = []

# Set the number of combinations for imaginary portfolios
num_assets = len(data.columns)
num_portfolios = 10000

for i in range(num_portfolios):
    
    weights = np.random.rand(num_assets) #get random weights for each stock
    weights /= sum(weights) #sum(weights) = 1
    
    portfolio = logreturns * weights #construct weighted portfolio
    
    returns = portfolio.sum(axis = 1) #rowsums
    risk_ind = returns.std()
    return_ind = sum(returns)
    
    
    
    port_returns.append(return_ind)
    port_risk.append(risk_ind)
    port_weights.append(weights)

portfolio = {"Returns": port_returns,
             "Risk": port_risk}


plt.scatter(portfolio["Returns"], portfolio["Risk"], s = 0.1)
plt.show()

sns.scatterplot(portfolio["Returns"], portfolio["Risk"])



