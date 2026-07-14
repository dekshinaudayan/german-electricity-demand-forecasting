# German Electricity Demand Forecasting

## Project Overview

This project investigates German electricity demand forecasting using statistical, machine learning, and deep learning techniques. The objective is to compare different forecasting approaches for predicting electricity demand using data from the Open Power System Data (OPSD) project.

The project was completed as part of the MSc Data Science programme.

## Forecasting Models

The following models were implemented:

- Exploratory Data Analysis (EDA)
- Stationarity Analysis
- Benchmark Forecasting Models
- SARIMA
- SARIMAX with Temperature Features
- Feature-Based Regression (XGBoost)
- Long Short-Term Memory (LSTM)

## Dataset

The project uses the **Open Power System Data (OPSD)** time series dataset.

Original dataset:

https://data.open-power-system-data.org/time_series/

The original dataset is not included in this repository because it exceeds GitHub's file size limit.

The notebooks automatically download the original dataset or use the processed datasets included in the repository.

## Repository Structure

```
data/
    Processed datasets

notebooks/
    Jupyter notebooks for Parts 1–6

outputs/
    Figures, forecasts and evaluation metrics

report/
    Final project report (PDF)

README.md
```

## Evaluation Metrics

The forecasting models were evaluated using:

- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)

## Report

The complete project report is available in the **report** folder.

## Author

Dekshina Udayan

MSc Data Science
