import csv
import requests
from bs4 import BeautifulSoup

# this function get header of the table and fill CSV header
def fetch_header_to_csv(url, csv_file_name):
    url = requests.get(url)
    soup = BeautifulSoup(url.text, 'html.parser')
    # fetch search table in table var
    table = soup.find('table', attrs={'class': 'table table-bordered table-hover table-custom fixed'})
    # getting All Column For Header
    get_th_row = table.findAll('th')
    print(get_th_row)
    table_item = []
    # Looping for appending text to list Headers
    for h in get_th_row:
        table_item.append(h.text.strip())

    # add header to CSV file
    file = open(csv_file_name, 'a', newline='', encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(table_item)
    file.close()

# this function get table conect of each page and fill CSV body
def fetch_table_to_csv(url_page, url_remain, csv_file_name):
    # for support paging
    ishavenextPage = True
    page = 1
    while ishavenextPage:
        url1 = f"https://www.rond.ir/SearchSim?page={page}"
        url = url1 + url_remain
        url_main = requests.get(url)
        # print(url_main)
        csv_file = csv_file_name
        soup = BeautifulSoup(url_main.text, 'html.parser')
        # fetch search table in table var
        table = soup.find('table', attrs={'class': 'table table-bordered table-hover table-custom fixed'})

        # open CSV file
        file = open(csv_file, 'a', newline='', encoding='utf-8-sig')
        # Fetch all tr in table
        table_body = table.findAll('tr')[1:]

        # looping for filling data in table from the first index to the last
        for j in table_body:
            row_data = j.findAll('td')
            row = [tr.text.strip() for tr in row_data]
            writer = csv.writer(file)
            writer.writerow(row)

        # print("page---", page, "---page")
        if soup.find("li", class_='PagedList-skipToNext') is None:
            ishavenextPage = False
        page += 1

        file.close()

