from crawler import Crawler
import extractor

def main():
    groupID = 8931
    website_url = f'https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{groupID}'

    crawler = Crawler()
    crawler.load_page(website_url)
    crawler.load_table_data()
    html = crawler.get_page_source()

    extractor.extract_data_to_csv(html, f'group_{groupID}')


if __name__ == '__main__':
    main()
