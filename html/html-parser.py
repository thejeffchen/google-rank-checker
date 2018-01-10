from bs4 import BeautifulSoup
import csv

yourpath = 'html'
html_files = []

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    html_files.append(f)

print(html_files)

for each_file in html_files:
    with open(each_file, 'rb') as file:
        print(each_file)
        soup = BeautifulSoup(file, "lxml")
        results = soup.find_all("h3", class_="r")
        for each_result in results:
            each_meta_title = each_result.text
            print(each_meta_title)
            link = each_result.find('a')
            print(link.get('href'))


    with open('keyword_rankings.csv', 'w') as csvfile:
        fieldnames = [
            'keyword', 
            'source 1',
            'source 2',
            'source 3',
            'source 4',
            'source 5',
            'source 6',
            'source 7',
            'source 8',
            'source 9',
            'source 10',
            'source 11',
            'source 12',
            'source 12',
            'source 13',
            'source 14',
            'source 15',
            'source 16',
            'source 17',
            'source 18',
            'source 19',
            'source 20',
            ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for each_html_file in html_files:
            writer.writerow({'keyword': str(each_html_file), 'source 1': 'Beans'})
