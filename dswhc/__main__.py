from contextlib import suppress
from json import load
from os import mkdir
from typing import Any

from . import google_calendar
from .crawler import Crawler
from .extractor import extract_data

URL = "https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{id}"


def load_cfg(file: str) -> dict[str, Any]:
    try:
        with open(file, "r") as f:
            return load(f)
    except FileNotFoundError:
        exit(f"Config file {file} not found!")


def prepare_folders() -> None:
    # check if folders exist and create them if they don't
    for folder in ["data", "data/extracted", "data/google_calendar"]:
        with suppress(FileExistsError):
            mkdir(folder)


def main() -> None:
    cfg = load_cfg("config.json")

    prepare_folders()

    dsw_crawler = Crawler(headless=cfg["headless"])

    for group_id in cfg["groupIDs"]:
        try:
            dsw_crawler.load_page(URL.format(id=group_id))
            dsw_crawler.load_table_data()
            html = dsw_crawler.page_source

            #  get raw data from html
            raw_data = extract_data(html)

            # cache data
            raw_data.to_csv(f"data/extracted/group_{group_id}.csv", index=False)

            gcal = google_calendar.convert_to_gcal(raw_data)

            if cfg["export"]["google"]["csv"]:
                gcal.to_csv(
                    f"data/google_calendar/calendar_group_{group_id}.csv", index=False
                )

        except Exception as e:
            print(f"Error while processing group {group_id}: {e}")
            print("Skipping...")

    dsw_crawler.close()


if __name__ == "__main__":
    main()
