import csv
import datetime
import requests
from bs4 import BeautifulSoup

# outline:
# 1) Наименование продукта(title).
# 2) Цена продукта(KGS).
# 3) Ссылка на фотку.


HOST = 'https://www.kivano.kg'
main_url = 'https://www.kivano.kg/mobilnye-telefony' 
file_name = 'telepon.csv'


def get_html(url, params = ''):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', 'item product_listbox oh')
    tels = []


    for item in items :
        tels.append(
            {
                'name' : item.find('div', 'listbox_title oh').find('a').get_text(strip = True),
                'tsena' : item.find('div', 'listbox_price text-center').find('strong').get_text(strip = True),
                'image' : HOST + item.find('div', 'listbox_img pull-left').find('img').get('src')

            }
        )
    return tels
def write_csv(items, path):
    with open(path, 'a', newline='' ) as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['name', 'tsena', 'photo'])

        for item in items:
            writer.writerow([item['name'], item['tsena'], item['image']])
        # writer.writerow([tels['name'],tels['tsena'], tels['image']])
        # print([tels['name'],tels['tsena'], tels['image']], 'parsed')

    
    
    # find('div', class) ---> find
    # find_all('div') ----> find_all

def main():
    tels = []
    start = datetime.datetime.now()
    html_text = get_html(main_url)
    tels.extend(get_total_pages(html_text))
    
    write_csv(tels, file_name)
    end = datetime.datetime.now()
    res = end - start
    print(str(res))


if __name__ == '__main__':
    main()

















