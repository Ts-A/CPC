# heatmap on a randomly generated set of values
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
  
data_set = np.random.rand( 10 , 10 )
ax = sns.heatmap( data_set , linewidth = 0.5, xticklabels='auto', yticklabels='auto', cmap = 'coolwarm' )
  
plt.title( "A1_Q8 Heat Map" )
plt.xlabel("Dataset X")
plt.ylabel("Dataset Y")
plt.show()