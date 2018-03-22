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

4) Run the script
```
python3 google-rank-checker.py
```

5) Go to the HTML folder and open keywords_rankings.csv

### Important Limitations
1) This is only for small scale rank checking, it goes at around ~6 terms a minute to be a good citizen of Google. I'm sure you can build out a large scale scraping operation with hundreds of AWS EC2 instances and thousands of proxies, but if you know how to do that, you probably don't need this script.
2) This only looks at the 1st page of search results. This was built for a specific project and I just needed to look at the first page. I might consider writing something that goes to the other pages, but it isn't built right now.
3) This only gives you the URLs of the first page of search results. Again, I only needed the URLs for this specific project
4) This could be limited to personalized and/or local search since it is just opening a normal Google browser. It isn't perfect, but it will give you a good enough measure of approximately what is ranking on the first page.

### Advanced / Troubleshooting
* **Want to switch user-agent?**

On line 32 of google-rank-checker.py you will see an option called "user-agent=...". Right now it is set at the standard Chrome agent. You should be able to change it to whichever user agent you are looking for. Just in case, there is a full list of Googlebot user agents here: https://support.google.com/webmasters/answer/1061943?hl=en

* **Chromedriver Problems?** You might need to install Chromedriver: 
https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/

Note: I also wrote most of the script in a few hours so it isn't perfect, but all feedback is welcome!