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
csv_path = csv_dir / 'final_error_constant_noise.csv'
csv_path = csv_dir / 'final_error_constant_outliers.csv'
csv_path = csv_dir / 'single_anchor_full.csv'

import pandas as pd
import numpy as np
from pathlib import Path

# # Example Usage:
# csv_path = 'fake_data.csv'  # You can specify your desired path here
# create_fake_csv(csv_path)

# Load the data
data = pd.read_csv(csv_path, header=None)

# Assign column names
data.columns = ['nb_measurements', 'noise_variances', 'outlier_probability', 'Linear', 'Non-linear', 'Final']

# Create a plot with the trend of the final error as a function of the noise variance
# The plot should be a simple line plot with the noise variance on the x-axis and the final error on the y-axis

def plot_error_trend(data, x_column, bin_width=0.05, cap_length=0.01):
    """
    Plot the final error trend as a function of the specified x_column (noise_variances or outlier_probability).
    
    Parameters:
    - data: DataFrame with the necessary columns
    - x_column: The column name for the x-axis ('noise_variances' or 'outlier_probability')
    - bin_width: The width of the bins for grouping the x_column values
    - cap_length: The length of the caps on the vertical error bars
    """
    # Bin the x_column into intervals
    data['x_bin'] = (data[x_column] // bin_width) * bin_width  # Group into bins

    # Compute mean and variance of final error for each x_bin
    summary = data.groupby('x_bin')['Final'].agg(['mean', 'var']).reset_index()

    # --- PLOTTING ---
    plt.figure(figsize=(10, 6))

    # Line plot of mean final error
    sns.lineplot(x=summary['x_bin'], y=summary['mean'], marker='o', label='Mean Final Error', color='red')

    # Plot vertical lines for variance (error bars) with caps at the ends
    for i, row in summary.iterrows():
        # Calculate the lower and upper bound for the variance
        lower_bound = row['mean'] - np.sqrt(row['var'])
        upper_bound = row['mean'] + np.sqrt(row['var'])
        
        # Plot a vertical line representing the variance
        plt.plot([row['x_bin'], row['x_bin']], [lower_bound, upper_bound], color='blue', alpha=0.7)
        
        # Add caps to the vertical lines
        plt.plot([row['x_bin'] - cap_length, row['x_bin'] + cap_length], [lower_bound, lower_bound], color='blue', alpha=0.7)
        plt.plot([row['x_bin'] - cap_length, row['x_bin'] + cap_length], [upper_bound, upper_bound], color='blue', alpha=0.7)

    # Labels and Title
    plt.xlabel(x_column.replace('_', ' ').title())  # Format the x_label
    plt.ylabel('Final Error')
    plt.title(f'Final Error vs {x_column.replace("_", " ").title()}')
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent label clipping
    plt.show()
# Call the function to plot the error trend for noise variance
plot_error_trend(data, 'noise_variances', bin_width=0.05, cap_length=0.01)

# Call the function to plot the error trend for outlier probability
plot_error_trend(data, 'outlier_probability', bin_width=0.01, cap_length=0.002)