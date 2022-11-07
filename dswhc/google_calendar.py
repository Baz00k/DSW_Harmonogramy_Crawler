import pandas as pd


def convert_to_csv(input_file_path: str, output_file_path: str) -> None:
    # load data from csv file
    df = pd.read_csv(input_file_path)

    # create title of the event from form of class and subject
    df["Subject"] = df["Form Of Class"] + ": " + df["Subject"]

    # create description of the event
    df["Description"] = (
        "Wykładowca: "
        + df["Lecturer"]
        + "\n"
        + "Komentarze: "
        + df["Comments"]
        + "\n"
        + "Czas trwania: "
        + df["Number Of Hours"]
    )

    # if there is no location, set it to online
    df["Location"] = df["Location"].fillna("Zdalnie")

    # convert to google calendar format by dropping unnecessary columns and renaming the rest
    df = df.drop(
        columns=[
            "Day Of Week",
            "Number Of Hours",
            "Form Of Class",
            "Group",
            "Lecturer",
            "Form Of Passing",
            "Mode Of Studies",
            "Comments",
        ]
    )
    df["Private"] = "True"
    df["All Day Event"] = "False"

    # save to csv file
    df.to_csv(f"data/calendar/{output_file_path}", index=False)
