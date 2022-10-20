from crawler.crawler import Crawler
from extractor.extractor import extract_data_to_csv
from calendarConverter.calendarConverter import convertToGoogleCalendarCSV

def main():
    dsw_crawler = Crawler(headless=True)
    groupRange = range(8931, 8932)

    for groupID in groupRange:
        website_url = f'https://harmonogramy.dsw.edu.pl/Plany/PlanyGrup/{groupID}'
        try:
            dsw_crawler.load_page(website_url)
            dsw_crawler.load_table_data()
            html = dsw_crawler.get_page_source()
            # cache data
            extract_data_to_csv(html, f'group_{groupID}')
            # convert to google calendar csv
            convertToGoogleCalendarCSV(f'data/extracted/group_{groupID}.csv', f'calendar_group_{groupID}.csv')

        except Exception as e:
            print(f'Error while processing group {groupID}: {e}')
            print('Skipping...')
    


if __name__ == '__main__':
    main()
