# 📊 Futures Market Data Analyzer

This project scrapes futures market data, performs analysis (like calculating mean prices), visualizes trends, and exports everything to Excel — all neatly following OOP and SOLID principles.

---

## 🔧 Features

- 📈 Calculates the **Mean** of High and Low prices for each contract.
- 📉 Plots **High, Low, and Mean** values in a line graph.
- 📌 Finds the contract with the **largest price change**.
- 📤 Exports the cleaned dataset to an Excel file (`futures_data.xlsx`) with the sheet named **Raw Data**.
- 🖼️ Saves the plot as `futures_comparison_plot.png` in the same directory.

---

## 🧱 Project Structure

├── futures_data_cleaner.py ├── futures_data_analyzer.py ├── futures_data_plotter.py ├── excel_exporter.py ├── main.py ├── futures_comparison_plot.png ├── futures_data.xlsx └── README.md



### 1. Install Dependencies

Ensure you have Python 3.7+ installed.

Install all required libraries using:

```bash
pip install -r requirements.txt


2. Run the Project
To execute the full pipeline:

python .\run.py