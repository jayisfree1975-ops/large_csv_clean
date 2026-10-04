Automated Data Cleaning Pipeline (5,000-Row Customer Dataset)

A robust Python data cleaning script built with Pandas and Regex to clean, standardize, and audit a messy, synthetic 5,000-row e-commerce dataset.

This repository demonstrates raw Python data engineering fundamentals—taking unformatted, noisy transactional data and producing a pristine, production-ready CSV output.

🛠️ The Problem

Raw data exports from enterprise CRMs or databases often contain corrupted formats, whitespace noise, inconsistent date types, and duplicate entries.

The original dataset (messy_customer_data_5k.csv) presented several real-world data issues:

Text Noise: Leading/trailing whitespace and multiple consecutive spaces in names and cities (e.g., "  John   Doe  ").

Mixed Date Formats: Inconsistent date representations across records (e.g., mixing YYYY-MM-DD and MM/DD/YYYY).

Unformatted Currency: Price columns formatted as text strings with symbols and commas (e.g., " $1,250.00 ").

Missing Critical Fields: Rows missing vital identifiers like state or phone numbers.

Duplicate Records: Exact duplicate rows caused by system sync errors.

💡 The Solution & Pipeline

The Python pipeline processes the 5,000 records through a targeted transformation sequence:

[Raw Messy CSV] ➡️ [Text Normalization] ➡️ [Mixed Date Stanpudardization] ➡️ [Regex Currency Cleaning] ➡️ [Targeted Missing Drop] ➡️ [Deduplication] ➡️ [Clean CSV Outt]


Key Transformation Steps:

String Hygiene: Cleans string columns (customer_name, city) using regex pattern replacement (\s+) to trim whitespace and reduce multi-space gaps to single spaces.

Date Parsing: Standardizes dates into strict YYYY-MM-DD string format using pd.to_datetime(format="mixed", errors="coerce").

Numeric Casts via Regex: Strips dollar signs ($) and commas (,) from unit_price using regex regex stripping before casting to float.

Data Integrity Audit: Drops rows missing core contact fields (state, phone_number).

Deduplication: Identifies and drops exact row duplicates to prevent duplicate record counts.

📁 Repository Structure

large_csv_clean/
│
├── data/
│   ├── messy_customer_data_5k.csv       # Raw input dataset (5,000 rows)
│   └── spreadsheet_5k_cleaned.csv       # Processed, clean deliverable
│
├── clean_data.py                        # Core cleaning pipeline script
└── README.md                            # Project documentation


💻 How to Run

Requirements

Python 3.8+

pandas

numpy

Quickstart

Clone this repository:

git clone https://github.com/your-username/large-csv-cleaner.git
cd large-csv-cleaner


Run the script:

python clean_data.py


📈 Roadmap & Progression

[x] v1.0 (Current): Procedural Pandas pipeline with regex string/currency parsing.

[ ] v1.1 (Next Release): Refactor pipeline to integrate into custom MakeSheet Object-Oriented Class module.

[ ] v1.2: Add automated exception logging and export directly to multi-tab formatted Excel sheets (openpyxl).

👤 Author

Python Automation & Data Cleaning Specialist

Available for freelance data engineering, web scraping, and spreadsheet automation projects.