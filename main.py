from crawler.crawler import Crawler
from extractor.extractor import extract_data_to_csv

def main():
    dsw_crawler = Crawler(headless=True)

    for groupID in range(8900, 8950):
        website_url = f'https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{groupID}'
        try:
            dsw_crawler.load_page(website_url)
            dsw_crawler.load_table_data()
            html = dsw_crawler.get_page_source()
            extract_data_to_csv(html, f'group_{groupID}')
        except:
            print(f'Group {groupID} not found')


if __name__ == '__main__':
    main()
