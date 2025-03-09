import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.kernel_ridge import KernelRidge

from pathlib import Path

package_path = Path(__file__).parent.parent.resolve()
csv_dir = package_path / 'csv_files'
csv_path = csv_dir / 'trajectory_optimisation_comparison.csv'

# Load the data
data = pd.read_csv(csv_path, header=None)

data.columns = ['Linear', 'Non-linear', 'FIM', 'GDOP']

# Create a box plot for each column
plt.figure(figsize=(10, 3))
sns.boxplot(data=data,
        boxprops=dict(facecolor='white', edgecolor='black'), 
        whiskerprops=dict(color='black'), 
        capprops=dict(color='black'), 
        medianprops=dict(color='black'), 
        flierprops=dict(marker='x', markeredgecolor='r', markersize=5)
    )
plt.xlabel('Estimation method')
plt.ylabel('Error in estimate', fontsize=12)
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
plt.xticks(fontsize=12)
plt.yticks(fontsize=10)
plot_save_path = 'trajectory_optimisation_comparison_boxplot.png'
plt.savefig(plot_save_path)
plt.show()