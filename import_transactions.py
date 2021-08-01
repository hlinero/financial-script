from pandas import pandas as pd

def import_transactions(list_of_filenames):
    list_of_df = []

    for filename in list_of_filenames:
        df_local = pd.read_csv(filename)
        list_of_df.append(df_local)

    df_total = pd.concat(list_of_df)
    df_total.reset_index(inplace = True)

    return df_total