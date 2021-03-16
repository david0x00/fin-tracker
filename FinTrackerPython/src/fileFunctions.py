import pandas as pd
from datetime import datetime

def readCSV(file):
    return pd.read_csv(file, keep_default_na=False)

def writeCSV(df, filename):
    df.to_csv(filename, index=False)

def getColumnList(df, index_name):
    return df[index_name].tolist()