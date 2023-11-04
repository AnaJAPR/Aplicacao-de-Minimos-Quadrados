import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Sleep_Efficiency.csv').dropna()
print(data)

Sleep_efficiency = data['Sleep efficiency'].values
Sleep_duration = data['Sleep duration'].values

plt.figure()
plt.scatter(Sleep_efficiency, Sleep_duration)
plt.xlabel('Sleep_efficiency')
plt.ylabel('Sleep_duration')
plt.show()
