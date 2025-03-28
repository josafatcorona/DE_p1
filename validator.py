"""This modules calls library module functions to apply taxes"""

from library.apply_taxes import read_client_config, apply_formulas
import pandas as pd

if __name__ == "__main__":
    path_file = "files/clientes_formulas.csv"
    # Example DataFrame with client data
    data = {
        "client": [1, 2, 3, 2],
        "vat_out": [10, 10, 10, 10],
        "special_out": [10, 10, 10, 10],
        "special_in": [10, 10, 10, 10],
    }
    df = pd.DataFrame(data)
    for i in range(1, 4):
        print(f"Client: {i}", "-" * 120)
        print(df)
        config = read_client_config(path_file, i)
        print(config)
        apply_formulas(json_formulas=config, df=df)
        print("-" * 120, "\n")
