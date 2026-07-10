import pandas as pd


def load_data(file_name):

    df = pd.read_csv(
        file_name,
        index_col=0
    )

    names = list(df.index)

    matrix = df.values.tolist()

    return names, matrix
