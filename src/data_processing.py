"""
Utility functions for loading and preprocessing electricity demand data.
"""

import pandas as pd


def load_dataset(filepath):
    """
    Load electricity demand dataset.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Dataset indexed by timestamp.
    """

    data = pd.read_csv(
        filepath,
        parse_dates=["timestamp"],
        index_col="timestamp"
    )

    return data


def aggregate_weekly(data):
    """
    Aggregate hourly electricity demand into weekly averages.

    Parameters
    ----------
    data : pandas.DataFrame
        Hourly electricity demand data.

    Returns
    -------
    pandas.DataFrame
        Weekly aggregated data.
    """

    return data.resample("W").mean()


def split_train_test(data, forecast_horizon):
    """
    Split a dataset into training and testing sets.

    Parameters
    ----------
    data : pandas.DataFrame
        Input dataset.

    forecast_horizon : int
        Number of observations used for testing.

    Returns
    -------
    train : pandas.DataFrame
        Training dataset.

    test : pandas.DataFrame
        Testing dataset.
    """

    train = data.iloc[:-forecast_horizon]

    test = data.iloc[-forecast_horizon:]

    return train, test
