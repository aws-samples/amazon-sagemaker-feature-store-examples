
import pandas as pd
import numpy as np

def choose_persona(row):
    if row['Id'] > 3:
        return 0
    else:
        return 1

def apply_transforms(df: pd.DataFrame) -> pd.DataFrame:
    df['Persona'] = df.apply(lambda row : choose_persona(row), axis=1) 
    df['NewFeature1'] = df['Persona'] * np.random.rand() + (2* df['ZipCode'])
    return df
