"""this modules has everything related with apply taxes to df"""

import pandas as pd


def read_client_config(path, client):
    """Docstring"""
    config = pd.read_csv(path)
    config = config[config.client == client]
    json_config = config.set_index("client")["formula"].to_dict()
    return json_config


import pandas as pd


def apply_formulas(json_formulas, df):
    """
    Applies formulas from a JSON dictionary to a pandas DataFrame.

    Parameters:
        json_formulas (dict): A dictionary with client as key and formula as value.
        df (pd.DataFrame): A DataFrame containing the data for calculations.

    Returns:
        pd.DataFrame: Updated DataFrame with a 'tax' column containing the results.
    """
    formula = next(iter(json_formulas.values()))
    print(f"The formula for this client is {formula}")
    df["tax"] = df.eval(formula)
    print(df)
