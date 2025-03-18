import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv(r'D:\Python\Matplotlib/WeatherData.csv')
top_10 = data.head(10)

# Plotting the data using the line plot
# plt.plot(top_10['Date'], top_10['Temperature'], color='red')
# plt.title('Temperature vs Date')
# plt.xlabel('Date')
# plt.ylabel('Temperature')
# plt.show()


# Plotting the data using the bar plot
plt.bar(top_10['Date'], top_10['Temperature'], color='blue')
plt.title('Temperature vs Date')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()