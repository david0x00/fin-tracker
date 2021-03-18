import pandas as pd
from datetime import datetime
import json
import locale

def readCSV(file):
    return pd.read_csv(file, keep_default_na=False)

def writeCSV(df, filename):
    df.to_csv(filename, index=False)

def getColumnList(df, index_name):
    return df[index_name].tolist()

def loadJSON(filename):
    with open(filename, 'r') as file:
        json_object = json.load(file)
    return json_object

def writeJSON(filename, json_object):
    with open(filename, 'w') as file:
        json.dump(json_object, file, indent=4)

def formatCurrency(value):
    return locale.currency(value, grouping=True)