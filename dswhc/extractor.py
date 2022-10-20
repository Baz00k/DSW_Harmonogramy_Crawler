from bs4 import BeautifulSoup
import pandas as pd


def extract_data(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("table#gridViewPlanyGrup_DXMainTable")
    assert table is not None  # so that the typechecker doesn't complain
    rows = table.find_all("tr")
    data: list[list[str | float]] = []
    date: str = ""
    day_of_the_week: str = ""

    for row in rows:
        # check if row is a header by checking its class
        if row.get("class") == ["dxgvGroupRow_Aqua"]:
            date = row.text.strip()
            # remove text before the date
            date = date.partition(":")[2].strip()
            # separate day of week from date
            date, day_of_the_week = date.split()
            continue

        cols: list[str | float] = [ele.text.strip() for ele in row.find_all("td")]
        # add date and day of week to the row
        cols = [date, day_of_the_week, *cols]
        # change empty strings to NaN
        cols = [ele or float("nan") for ele in cols]

        data.append(cols)

    df = pd.DataFrame(data)

    # Remove rows only for styling
    df = df.drop(df.head(12).index)

    # drop empty rows and columns
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    df.columns = [
        "Start Date",
        "Day Of Week",
        "Start Time",
        "End Time",
        "Number Of Hours",
        "Subject",
        "Form Of Class",
        "Group",
        "Location",
        "Lecturer",
        "Form Of Passing",
        "Mode Of Studies",
        "Comments",
    ]  # type: ignore

    return df


def extract_data_to_csv(html: str, filename: str) -> None:
    extract_data(html).to_csv(f"data/extracted/{filename}.csv", index=False)
