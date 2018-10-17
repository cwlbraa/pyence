import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('~/Documents/postgres-unindexed.csv', header=0, encoding='utf-8')

sns.set()
sns.set_style("darkgrid")

ax = sns.lineplot(x="labels", y="duration", hue="hue", data=data)
# ax = sns.lmplot(x='app_count',y='time',data=data, hue="label", fit_reg=True)
ax.set(xlabel="label_count", ylabel="Time (seconds)")
ax.set_title('labelin')
#ax.set_xscale('log')

plt.show()