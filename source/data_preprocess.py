import pandas as pd


class DataPreprocessing():
    def __init__(self):
        pass

    def load_data(path):
        data = pd.read_csv(path, sep="\t", header=None).dropna()

        print(data.head()) 

        data = data.to_numpy()

        return data

    data = load_data('/Users/Nguyener/Documents/GitHub/meters/data/Meter_A.txt')