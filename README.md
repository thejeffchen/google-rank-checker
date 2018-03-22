# Google Rank Checker

This python script will use your computer to check the real time Google search rankings for keywords. At a high level it does this by opening up an automated browser (Selenium), google searching the keyword, scraping the HTML, separating the HTML so you get a spreadsheet of all the URLs ranking for a keyword.

Note: this is relatively slow since we want to be good citizens of Google. Right now it goes at ~6 terms every minute.

Note: I wrote most of the script in a few hours so it isn't perfect, but all feedback is welcome!

## Getting Started

1) Open Terminal on Mac (Press 'command + space' and type in 'Terminal')

2) Install the files on your desktop folder

Type in the terminal:

```
cd desktop
```

3) Copy the files from the github
```
git clone git@github.com:thejeffchen/google-rank-checker.git
```

4) Install virtualenv and create a new virtual environment to keep all the packages separate from your desktop 

Instructions: http://sourabhbajaj.com/mac-setup/Python/virtualenv.html
```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

5) Open keywords.csv and add the keywords you want to check in column A

6) Install the requirements from the environment

```
pip3 install -r requirements.txt
```

7) Run the google scraper script
```
python3 google-scraper.py
```

You should see windows opening up and typing in search terms

8) Go to the HTML folder and open up keywords_rankings.csv to get your list of URLs!