# scrapy-etender

Scrape advertised tenders
  pipenv run scrapy crawl tenders -t csv -o tenders.csv

Scrape tender awards
  pipenv run scrapy crawl awards -t csv -o tender_awards.csv
  
Scrape cancelled tenders
  scrapy crawl cancelled -o cancelled_tenders.csv
  
Scrape closed tenders
  scrapy crawl closed -o closed_tenders.csv
