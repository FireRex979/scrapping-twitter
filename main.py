import snscrape.modules
import csv

tweets=snscrape.modules.twitter.TwitterSearchScraper(query='gamer indonesia')

with open('text.csv', 'a', encoding='utf-8') as f:
    wr=csv.writer(f, lineterminator = '\n')
    for i in tweets.get_items():
        print([i.content])
        wr.writerow([i.content])