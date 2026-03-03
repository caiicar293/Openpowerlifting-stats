OpenPowerlifting Performance Analyzer (SQL & Python)
This project provides a flexible framework for analyzing powerlifting strength distributions. It processes the OpenPowerlifting dataset using a hybrid approach—combining the speed of SQL (DuckDB) with the analytical depth of Pandas.

🛠 Key Features
Hybrid Data Pipeline: Uses DuckDB to write SQL queries directly on CSV files for efficient filtering and Pandas for complex statistical calculations.

Dynamic Weight Class Analysis: The logic is built to be easily adjusted across different weight classes and demographics (currently focused on the 67.5kg–75kg range but designed for easy parameter updates).

Statistical Benchmarking: Calculates performance percentiles (up to the 97th percentile) and Bodyweight Multipliers to define "elite" performance levels.

Automated Visualization: Generates distribution histograms for Squat, Bench, and Deadlift with automated Mean/Median/Mode and Standard Deviation overlays.

📊 Why SQL + Pandas?
Most real-world data is too large for Pandas alone. By using DuckDB, I demonstrate the ability to:

Query Data via SQL: Perform high-performance filtering and type-casting (TRY_CAST) before the data ever hits memory.

Analyze via Python: Use Pandas for the heavy lifting of feature engineering and statistical modeling.

🚀 Future Plans
Parameterized Inputs: Update the script to accept user-defined weight classes and equipment types as arguments.

Comparative Analysis: Add functionality to compare performance distributions across different weight classes side-by-side.
