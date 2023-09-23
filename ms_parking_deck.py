import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('/Users/bjuli/sparkasse/fi-crowd-mining/parking-decks-muenster/parking-decks-muenster/data/2020-06-07.csv')
    print(df.columns())
