import pandas as pd
def encode_genre(df):
    dictionary = {'rock':0,'edm':1,'pop':2,'r&b':3,'rap':4,'latin':5}
    cat_df = []
    cat_df = df.replace(dictionary)
    return pd.DataFrame(cat_df)
        