import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Load data
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 🔹 Line of best fit (ALL DATA)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = range(df['Year'].min(), 2051)
    sea_level_pred = res.slope * years_extended + res.intercept

    plt.plot(years_extended, sea_level_pred, color='red', label='Fit: All data')

    # 🔹 Line of best fit (FROM 2000)
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_recent = range(2000, 2051)
    sea_level_recent_pred = res_recent.slope * years_recent + res_recent.intercept

    plt.plot(years_recent, sea_level_recent_pred, color='green', label='Fit: 2000 onwards')

    # Labels
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.legend()

    # Save plot
    plt.savefig("sea_level_plot.png")

    return plt.gca()