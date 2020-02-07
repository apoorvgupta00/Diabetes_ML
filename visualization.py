import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
from matplotlib import pyplot as plt    
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('diabetes.csv')

print(df.head())


df.hist()
plt.tight_layout()
plt.show()


plt.subplots(3,3,figsize=(20,20))

for idx, col in enumerate(df.columns):
    ax = plt.subplot(3,3,idx+1)
    ax.yaxis.set_ticklabels([])
    sns.distplot(df.loc[df.Outcome == 0][col], hist=False, axlabel= False, kde_kws={'linestyle':'-', 'color':'black', 'label':"No Diabetes"})
    sns.distplot(df.loc[df.Outcome == 1][col], hist=False, axlabel= False, kde_kws={'linestyle':'--', 'color':'black', 'label':"Diabetes"})
    ax.set_title(col)

plt.subplot(3,3,9).set_visible(False)
plt.tight_layout()
plt.show()

