import pandas as pd
import matplotlib.pyplot as plt

# Sample data for stock prices of Alphabet Inc.
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Price': [1500, 1530, 1515, 1540, 1560]
}

# Convert data to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot the stock prices as a line plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Price'], marker='o')
plt.title('Alphabet Inc. Stock Price (Historical)')
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.grid(True)
plt.show()
