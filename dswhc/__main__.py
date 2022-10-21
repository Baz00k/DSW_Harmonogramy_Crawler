from .crawler import Crawler
from .extractor import extract_data_to_csv
from .calendar_converter import convert_to_google_calendar_csv

from json import load
from typing import Any
from contextlib import suppress
from os import mkdir


URL = "https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{id}"


def load_cfg(file: str) -> dict[str, Any]:
    try :
        with open(file, "r") as f:
            return load(f)
    except FileNotFoundError:
        print(f"Config file {file} not found!")
        exit(1)


def prepare_folders() -> None:
    # check if folders exist and create them if they don't
    for folder in ["data", "data/extracted", "data/calendar"]:
        with suppress(FileExistsError):
            mkdir(folder)


def main() -> None:
    prepare_folders()

    cfg = load_cfg("config.json")
    gr = cfg.pop("group_range")
    
    dsw_crawler = Crawler(**cfg)

    for group_id in range(gr[0], gr[1] + 1):
        try:
            dsw_crawler.load_page(URL.format(id=group_id))
            dsw_crawler.load_table_data()
            html = dsw_crawler.page_source
            # cache data
            extract_data_to_csv(html, f"group_{group_id}")
            # convert to google calendar csv
            convert_to_google_calendar_csv(
                f"data/extracted/group_{group_id}.csv", f"calendar_group_{group_id}.csv"
            )

        except Exception as e:
            print(f"Error while processing group {group_id}: {e}")
            print("Skipping...")

    dsw_crawler.close()


if __name__ == "__main__":
    main()
