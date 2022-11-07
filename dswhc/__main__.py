from contextlib import suppress
from json import load
from os import mkdir
from typing import Any

import google_calendar

from .crawler import Crawler
from .extractor import extract_data_to_csv

URL = "https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{id}"


def load_cfg(file: str) -> dict[str, Any]:
    try:
        with open(file, "r") as f:
            return load(f)
    except FileNotFoundError:
        exit(f"Config file {file} not found!")


def prepare_folders() -> None:
    # check if folders exist and create them if they don't
    for folder in ["data", "data/extracted", "data/calendar"]:
        with suppress(FileExistsError):
            mkdir(folder)


def main() -> None:
    prepare_folders()

    cfg = load_cfg("config.json")
    headless = cfg["headless"]
    group_range = cfg["group_range"]

    dsw_crawler = Crawler(headless=headless)

    for group_id in range(group_range[0], group_range[1] + 1):
        try:
            dsw_crawler.load_page(URL.format(id=group_id))
            dsw_crawler.load_table_data()
            html = dsw_crawler.page_source

            # cache data
            extract_data_to_csv(html, f"group_{group_id}")

            google_calendar.convert_to_csv(
                input_file_path=f"data/extracted/group_{group_id}.csv",
                output_file_path=f"calendar_group_{group_id}.csv",
            )

        except Exception as e:
            print(f"Error while processing group {group_id}: {e}")
            print("Skipping...")

    dsw_crawler.close()


if __name__ == "__main__":
    main()
