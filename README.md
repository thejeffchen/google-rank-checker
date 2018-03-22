# Google Rank Checker

This python script will use your computer to check the real time Google search rankings for the first page of search results for a small amount of keywords (I have tested around a few thousand keywords at once with no problems).

I wrote this because I work in SEO and need real time rankings and couldn't find any open source projects that worked or had a lot of features I didn't want.

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

### Important Limitations
1) This is only for small scale rank checking, it goes at around ~6 terms a minute to be a good citizen of Google. I'm sure you can build out a large scale scraping operation with hundreds of AWS EC2 instances and thousands of proxies, but if you know how to do that, you probably don't need this script.
2) This only looks at the 1st page of search results. This was built for a specific project and I just needed to look at the first page. I might consider writing something that goes to the other pages, but it isn't built right now.
3) This only gives you the URLs of the first page of search results. Again, I only needed the URLs for this specific project

Note: I also wrote most of the script in a few hours so it isn't perfect, but all feedback is welcome!