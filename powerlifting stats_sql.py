import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import duckdb
# Load the CSV file
df = pd.read_csv(r'.\openpowerlifting-2025-08-16-0862dc91.csv')


# Filter data for males, valid numeric values, and specific conditions
def is_numeric(column):
    return df[column].apply(lambda x: isinstance(x, (int, float)))

df = duckdb.sql("""
    SELECT *
    FROM df
    WHERE Sex = 'M'
      AND TRY_CAST(Best3DeadliftKg AS DOUBLE) IS NOT NULL
      AND TRY_CAST(Best3SquatKg AS DOUBLE) IS NOT NULL
      AND TRY_CAST(Best3BenchKg AS DOUBLE) IS NOT NULL
      AND BodyweightKg BETWEEN 67.5 AND 75
      AND Event = 'SBD'
      AND Equipment = 'Raw'
""").df()

meets = Counter(df['Name'])
times = Counter(meets.values())
samples = sum(times.values())
unique_entries = len(meets)

print("Number of unique entries:", unique_entries)
for x in sorted(times):
    print("Meets went:" ,x, 'Frequency:',times[x] , 'Percentage:', times[x] /samples )
    
    
# Plot histogram of the counts
plt.figure(figsize=(8, 6))
plt.bar(times.keys(), times.values(), edgecolor='black', alpha=0.7)
plt.title('Histogram of Occurrence Frequencies')
plt.xlabel('Number of Occurrences (Frequency)')
plt.ylabel('Number of Items')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print("Bodyweight:", df['BodyweightKg'].median())

# Create new columns for multipliers and percentages
df['Deadlift BW Multiplier'] = df['Best3DeadliftKg'] / df['BodyweightKg']
df['Squat BW Multiplier'] = df['Best3SquatKg'] / df['BodyweightKg']
df['Bench BW Multiplier'] = df['Best3BenchKg'] / df['BodyweightKg']

if 'TotalKg' in df.columns:
    for lift in ['Deadlift', 'Squat', 'Bench']:
        df[f'{lift} Percentage of Total'] = (df[f'Best3{lift}Kg'] / df['TotalKg']) * 100

# Function to calculate percentiles
def calculate_percentiles(column):
    return {
        '25th': column.quantile(0.25),
        '50th (Median)': column.quantile(0.50),
        '75th': column.quantile(0.75),
        '84th': column.quantile(0.84),
        '97th': column.quantile(0.97)
    }

# Generate and print percentiles for relevant columns
columns_to_analyze = ['BodyweightKg',
    'Deadlift BW Multiplier', 'Squat BW Multiplier', 'Bench BW Multiplier',
    'Deadlift Percentage of Total' , 'Squat Percentage of Total', 'Bench Percentage of Total',
    'Best3DeadliftKg', 'Best3SquatKg', 'Best3BenchKg', 'TotalKg', 'Wilks'
]

for column in columns_to_analyze:
    if column in df.columns:
        print(f"\n{column} Percentiles:")
        for percentile, value in calculate_percentiles(df[column]).items():
            print(f"{percentile}: {value}")

# Plot histograms for relevant columns
def plot_histogram(column, bins=100):
    # Calculate statistics
    median = np.median(column)
    mean = np.mean(column)
    mode = column.mode()[0]  # Mode can return multiple values, so we take the first one
    std_dev = np.std(column)

    # Create histogram plot
    plt.figure(figsize=(8, 6))
    plt.hist(column, bins=bins, edgecolor='black', alpha=0.7)
    plt.title(f'Histogram of {column.name}')
    plt.xlabel(column.name)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add the statistics on the graph
    plt.axvline(median, color='r', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
    plt.axvline(mean, color='g', linestyle='dashed', linewidth=1, label=f'Average: {mean:.2f}')
    plt.axvline(mode, color='b', linestyle='dashed', linewidth=1, label=f'Mode: {mode:.2f}')
    
    # Display the standard deviation as a shaded area or line
    plt.axvline(mean + std_dev, color='orange', linestyle='dotted', linewidth=1, label=f'+1 Std Dev: {mean + std_dev:.2f}')
    plt.axvline(mean - std_dev, color='orange', linestyle='dotted', linewidth=1, label=f'-1 Std Dev: {mean - std_dev:.2f}')

    # Show legend
    plt.legend()

    # Show plot
    plt.show()

columns_to_plot = ['BodyweightKg',
    'Deadlift BW Multiplier', 'Squat BW Multiplier', 'Bench BW Multiplier',
    'Deadlift Percentage of Total' , 'Squat Percentage of Total', 'Bench Percentage of Total',
    'Best3DeadliftKg', 'Best3SquatKg', 'Best3BenchKg', 'TotalKg', 'Wilks'
]
for column in columns_to_plot:
    if column in df.columns:
        plot_histogram(df[column])

# Print the number of samples
print(f"\nNumber of samples: {df.shape[0]}")
