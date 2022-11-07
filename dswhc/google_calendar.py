import pandas as pd


def convert_to_gcal(raw_data: pd.DataFrame) -> pd.DataFrame:
    gcal = pd.DataFrame(
        columns=[
            "Subject",
            "Description",
            "Location",
            "Start Date",
            "Start Time",
            "End Time",
            "All Day Event",
            "Private",
        ]
    )

    # create title of the event from form of class and subject
    gcal["Subject"] = raw_data["Form Of Class"] + ": " + raw_data["Subject"]

    # create description of the event
    gcal["Description"] = (
        "Wykładowca: "
        + raw_data["Lecturer"]
        + "\n"
        + "Komentarze: "
        + raw_data["Comments"]
        + "\n"
        + "Ilość godzin lekcyjnych: "
        + raw_data["Number Of Hours"]
    )

    gcal["Start Date"] = raw_data["Start Date"]
    gcal["Start Time"] = raw_data["Start Time"]
    gcal["End Time"] = raw_data["End Time"]

    # if there is no location, set it to online
    gcal["Location"] = raw_data["Location"].fillna("Zdalnie")

    # Add event metadata
    gcal["All Day Event"] = "False"
    gcal["Private"] = "True"

    return gcal


def add_to_calendar():
    pass
