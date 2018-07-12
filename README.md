# Google Rank Checker

This python script will use your computer to check the real time Google search rankings for the first page of search results for keywords (I have tested around a few thousand keywords at once with no problems).

I wrote this because I work in SEO and needed real time rankings from a lot of keywords on demand. A lot of rank tracking software seemed to have outdated rankings or never seemed to match what I was seeing. I also couldn't find any open source projects that worked or had a lot of features I didn't want. Hopefully others find this useful!

## Getting Started

1) Open Terminal on Mac (Press 'command + space' and type in 'Terminal')

2) Install the files on your desktop folder

Type in the terminal:

```
cd desktop
```

3) Copy the files from the github and switch to that folder
```
git clone git@github.com:thejeffchen/google-rank-checker.git
cd google-rank-checker
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
python3 google-rank-checker.py
```

You should see windows opening up and typing in search terms

8) Go to the HTML folder and open up keywords_rankings.csv to get your list of URLs!

## Run Again and Again

1) Open Terminal on Mac (Press 'command + space' and type in 'Terminal')

2) Change directory to google-rank-checker
```
cd desktop
cd google-rank-checker
```

3) Start the virtual environment
```
source venv/bin/activate
```

4) Add your new keywords in keywords.csv

5) Delete the old HTML files from the HTML folder so the keyword_rankings.csv only gives you rankings for keywords you just searched

6) Run the script
```
python3 google-rank-checker.py
```

7) Go to the HTML folder and open keywords_rankings.csv

## Important Limitations
1) This is only for small scale rank checking, it goes at around ~6 terms a minute to be a good citizen of Google. I'm sure you can build out a large scale scraping operation with hundreds of AWS EC2 instances and thousands of proxies, but if you know how to do that, you probably don't need this script.
2) This only looks at the 1st page of search results. This was built for a specific project and I just needed to look at the first page. I might consider writing something that goes to the other pages, but it isn't built right now.
3) This only gives you the URLs of the first page of search results. Again, I only needed the URLs for this specific project
4) This could be limited to personalized and/or local search since it is just opening a normal Google browser. It isn't perfect, but it will give you a good enough measure of approximately what is ranking on the first page.

## How Exactly Does the Script Work?

For the curious at a high level, the script works in 5 basic parts:
1) Import the CSV of keywords to check the rank for
2) For each keyword, use Selenium to open a new incognito Chrome browser and google search the keyword (HTML, CSS, JS, etc. is all rendering normally because it acts like a real browser)
3) Download all the source code from the first page and put it into a folder called html
4) Use a HTML parser (BeautifulSoup + lxml) to search through all the HTML in the folder 'html' and find the exact info of hrefs
5) Output a CSV of the URL ranks in the html folder

## Want to do bulk indexation checking?

Instead of putting keywords in keywords.csv, put "site:examplewebsite.com/slug" and you can see if Google has indexed the page!

## Advanced / Troubleshooting
* **I got stopped! Do I need to rerun the script for all keywords?**

Nope! 
1) Figure out the last keyword that was run by checking either the terminal output or look at the html folder and sort by Date Modified.
2) Remove all the keywords that have already been run from keywords.csv
3) Re run the python script

Doing this should restart the process from where you left off. As long as you leave the previously generated HTML files in the html folder, your keyword_rankings.csv file will still contain all the keywords.

* **Want to switch user-agent?**

On line 32 of google-rank-checker.py you will see an option called "user-agent=...". Right now it is set at the standard Chrome agent. You should be able to change it to whichever user agent you are looking for. Just in case, there is a full list of Googlebot user agents here: https://support.google.com/webmasters/answer/1061943?hl=en

* **Want to use proxies?**

Warning: Use at your own risk. Google seems to be pretty good at detecting proxy usage so only use good proxies. I was stopped fairly quickly.

This system will rotate randomly among however many proxies you put in

1) Add list of proxies to lines 12, 13, etc. using the format given. Make sure each proxy added is 'IP ADDRESS:PORT' (pay attention to the quotes and add a comma at the end between proxies)
2) Uncomment lines 40-42 to enable the proxies by removing the '#' sign

* **Want to change the rate of page checking?**

Change line 68 to vary the amount of time. The default setting picks a random integer between 1 and 4 seconds, but this can be set to any amount you wish. 

* **Chromedriver Problems?** 

You might need to install Chromedriver: 
https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/

Note: I also wrote most of the script in a few hours so it isn't perfect, but all feedback is welcome!