from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def extract_data(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one("table#gridViewPlanyGrup_DXMainTable")
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])

    
    df = pd.DataFrame(data)

    # Remove rows only for styling
    df = df.drop(df.head(12).index)
    
    # replece empty cells with NaN
    df.replace('', np.nan, inplace=True)

    # drop empty rows and columns
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    return df

def extract_data_to_csv(html: str, filename: str) -> None:
    data = extract_data(html) 
    data.to_csv(f'data/{filename}.csv', index=False, header=False)
    