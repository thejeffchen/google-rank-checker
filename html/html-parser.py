from bs4 import BeautifulSoup
import csv

yourpath = 'html'
html_files = []

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    html_files.append(f)

print(html_files)

# Create new .csv file
with open('keyword_rankings.csv', 'w') as myfile:
    writer = csv.writer(myfile, delimiter=',')
    writer.writerow(['Source', 'Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5', 'Rank 6', 'Rank 7', 'Rank 8', 'Rank 9', 'Rank 10', 'Rank 11', 'Rank 12', 'Rank 13', 'Rank 14', 'Rank 15', 'Rank 16', 'Rank 17', 'Rank 18', 'Rank 19', 'Rank 20'])
    myfile.close()

# Append each row to the .csv file
for each_file in html_files:
    if each_file.endswith(".html"):
        with open(each_file, 'rb') as file:
            print(each_file)
            soup = BeautifulSoup(file, "lxml")
            results = soup.find_all("h3", class_="r")
            list_of_ranks = []
            
            for each_result in results:
                each_meta_title = each_result.text
                link = each_result.find('a')
                link = link.get('href')
                list_of_ranks.append(link) # Add this back in for Meta Titles: + ' / ' + each_meta_title)
            print(list_of_ranks)

        with open('keyword_rankings.csv', 'a') as csvfile:
            csvfile.write('%s,' % each_file)
            for each_column in list_of_ranks:
                csvfile.write('%s,' % each_column)
            csvfile.write('\n')