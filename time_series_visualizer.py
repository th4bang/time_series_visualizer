import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Filter out the top and bottom 2.5% of the data based on page views
lower_percentile = df['page_views'].quantile(0.025)
upper_percentile = df['page_views'].quantile(0.975)
df_filtered = df[(df['page_views'] >= lower_percentile) & (df['page_views'] <= upper_percentile)]

# Draw Line Plot
def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df_filtered.index, df_filtered['page_views'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.show()

# Draw Bar Plot
def draw_bar_plot():
    df_filtered['year'] = df_filtered.index.year
    df_filtered['month'] = df_filtered.index.month
    df_monthly = df_filtered.groupby(['year', 'month'])['page_views'].mean().unstack()
    df_monthly.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Monthly Page Views by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.tight_layout()
    plt.show()

# Draw Box Plot
def draw_box_plot():
    df_filtered['year'] = df_filtered.index.year
    df_filtered['month'] = df_filtered.index.month
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
    sns.boxplot(x='year', y='page_views', data=df_filtered, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    sns.boxplot(x='month', y='page_views', data=df_filtered, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    plt.tight_layout()
    plt.show()

# Run the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
