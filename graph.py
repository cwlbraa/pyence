import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

filename = 'data/postgres-linearx0.csv'
data = pd.read_csv(filename, header=0, encoding='utf-8')

sns.set()
sns.set_style("darkgrid")

ax = sns.lineplot(x="label_count", y="duration", hue="hue", data=data)
# ax = sns.lmplot(x='app_count',y='time',data=data, hue="label", fit_reg=True)
ax.set(xlabel="label_count", ylabel="Time (seconds)")
ax.set_title(filename)
#ax.set_xscale('log')

plt.show()
plt.savefig(filename+'.svg', type='svg')