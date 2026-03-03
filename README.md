

# OpenPowerlifting: Multi-Method Data Analysis (SQL vs. Pandas)

This project explores performance distributions within the **OpenPowerlifting** dataset. Rather than a single pipeline, this repository demonstrates **two independent architectural approaches** to the same analytical problem.

## 🏗 Dual-Implementation Strategy

I have provided two versions of the analysis to showcase versatility in different technical environments:

### 1. The Pythonic Approach (Pandas)

* **Performance:** Optimized for speed on local datasets using vectorized operations.
* **Focus:** Leverages `Boolean Indexing` and `apply()` functions for rapid data filtering and feature engineering.
* **Best For:** Fast, interactive analysis on local machines where RAM is sufficient.

### 2. The Relational Approach (DuckDB/SQL)

* **Architecture:** Uses the **DuckDB** engine to run SQL queries directly on CSV files.
* **Focus:** Demonstrates proficiency in `TRY_CAST`, complex `WHERE` clauses, and relational logic.
* **Best For:** Environments where data lives in a database or exceeds local memory limits, requiring server-side filtering.

## 📊 Analytical Scope

Both methods are designed to be **modular** and **adjustable** for future weight-class comparisons:

* **Dynamic Filtering:** Currently tuned for the 67.5kg–75kg range but built to be easily parameterized.
* **Strength Benchmarking:** Calculates 25th to 97th percentiles and Bodyweight Multipliers.
* **Statistical Visualization:** Generates histograms with automated Mean, Median, and Standard Deviation markers.

## 🛠 Setup & Usage

1. **Dependencies:** `pip install pandas matplotlib numpy duckdb`
2. **Data:** Place the OpenPowerlifting `.csv` in the root directory.
3. **Execute:** Choose either the SQL-based or Pandas-based script to generate the performance distribution.



