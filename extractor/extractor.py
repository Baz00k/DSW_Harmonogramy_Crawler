from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def extract_data(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one("table#gridViewPlanyGrup_DXMainTable")
    rows = table.find_all('tr')
    data = []
    date = ''
    day_of_week = ''

    for row in rows:
        # check if row is a header by checking its class
        if row.get('class') == ['dxgvGroupRow_Aqua']:
            date = row.text.strip()
            # remove text before the date
            date = date[date.find(':')+1:]
            # separate day of week from date
            day_of_week = date[12:]
            date = date[:11]
            continue

        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        # add date and day of week to the row
        cols.insert(0, date)
        cols.insert(1, day_of_week)
        # change empty strings to NaN
        cols = [np.nan if ele == '' else ele for ele in cols]
        data.append(cols)

    
    df = pd.DataFrame(data)

    # Remove rows only for styling
    df = df.drop(df.head(12).index)

    # drop empty rows and columns
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    columns=['Start Date', 'Day Of Week', 'Start Time', 'End Time', 'Number Of Hours', 'Subject', 'Form Of Class', 'Group', 'Location', 'Lecturer', 'Form Of Passing', 'Mode Of Studies', 'Comments']
    df.columns = columns

    return df

def extract_data_to_csv(html: str, filename: str) -> None:
    data = extract_data(html) 
    data.to_csv(f'data/extracted/{filename}.csv', index=False)
    