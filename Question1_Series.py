import pandas as pd
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])
#display both the series individually in the console
print(series1)
print(series2)
#Performing arithmetic operations
print("Add the two Series:")
series = series1 + series2
print(series)
print("Subtract the two Series:")
series = series1 - series2
print(series)
print("Multiply the two Series:")
series = series1 * series2
print(series)
print("Divide Series1 by Series2:")
series = series1 / series2
print(series)
print("Modulus Series1 by Series2:")
series = series1 % series2
print(series)
