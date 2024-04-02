import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_data(path, type):
    if type == 'EXCEL':
        df = pd.read_excel(path)
    elif type == 'CSV':
        df = pd.read_csv(path)
    else:
        return 0
    df.dropna(inplace=True)
    data = df.set_index('time', drop=True)
    return df, df.head(3), df.columns


# df = get_data_excel('D')