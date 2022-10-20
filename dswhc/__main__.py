from .crawler import Crawler
from .extractor import extract_data_to_csv
from .calendar_converter import convert_to_google_calendar_csv

import json
from typing import Any


def load_cfg(file: str) -> dict[str, Any]:
    with open(file) as f:
        return json.load(f)


def main():
    cfg = load_cfg("config.json")
    headless = cfg["headless"]
    group_range = cfg["group_range"]
    dsw_crawler = Crawler(headless=cfg["headless"])
    group_range = range(8931, 8932)

    for group_id in group_range:
        website_url = f"https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{group_id}"
        try:
            dsw_crawler.load_page(website_url)
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
