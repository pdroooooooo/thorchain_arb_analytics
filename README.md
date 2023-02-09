###### CEX - DEX Arb Analytics

## Overview

A data analytics tool to explore arbitrage opportunities between a liquid Centrilized Exchange (CEX) and a less-liquid cross-chain Decentralized Exchage (DEX)

Buit for the Ironhack DA FT Jan23 Mx Bootcamp.

## Objective

Analyze for patterns, try and predict price differencials between a liquid Centrilized Exchange (CEX) and a less-liquid cross-chain Decentralized Exchage (DEX) from data like dates, time and pools. Alternatively, to determine if more or richer samples are needed.

# Data Sources

The data in this project was extracted using python algorithms that log price differentials between Binance and THORChain - the two biggest trading venues in their respective categories - during a lapse of three days sarting on February 8th, 2023.

# Data analysis workflow 

1. After creating a pandas DataFrame from the .log file, data is analyzed for size and forms.
2. Data is generally clean but a unix timestamp column is added and several more are dropped.
3. Rows with price differentials insignificantly small are removed afterwards.
4. Data is divided into numerical, caterorical and datetime-based tables.
5. Numerical distributions are plotted using Seaborn module.
6. Correlation between numerical variables is explored visually using Seanorn's heatmap function.
7. Categorical data is treated with One-Hot encoding.
8. Categorical and numerical data are concatenated into a new table.
9. New table can be fed into a lineal regression model, from the sklearn module.
10. Model is trained and tested for validation.

Note: Full workflow is detailed in the code comments too. 

# Results

business analytic approach you used to solve the problem. 

# Other notes

1. If you are having trouble installing sklearn try with * pip install -U scikit-learn *
2. Both cex_price and dex_price distribution graphs behave unexpectedly.
grafica rara


