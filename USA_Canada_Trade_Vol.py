import pandas as pd 
import matplotlib.pyplot as plt

trade_data = pd.read_csv('trade_data.csv')
print(trade_data.head())

trade_data['Date'] = pd.to_datetime(trade_data['Date'])
pre_tariff_data = trade_data[trade_data['Date'] < '2018-01-01']
post_tariff_data = trade_data[trade_data['Date'] >= '2018-01-01']

plt.figure(figsize=(10, 6))
plt.plot(pre_tariff_data['Date'], pre_tariff_data['Trade_Value'], 
label='Pre-Tariff Trade Volume', color='blue')
plt.plot(post_tariff_data['Date'], post_tariff_data['Trade Volume'],
label='Post-Tariff Trade Volume', color='red')
plt.title("USA and Canada Trade Volume Before and After Tariffs")
plt.xlabel("Date")
plt.ylabel("Trade Volume in USD")
plt.legend()
plt.grid()
plt.show()

pre_tariff_

