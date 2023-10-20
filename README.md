# Top US University Data Scraping Project

### Description

Top US University data scraping project using Scrapy and collecting the data from the API.

### How to run

1. Install the dependencies

```bash
pip install scrapy jmespath
```

Or you can install the dependencies from the `requirements.txt` file

```bash
pip install -r requirements.txt
```

2. Run the Scrapy Crawler

```bash
scrapy crawl university
```

You also can add `-o` flag for outputting the result as csv or json like the code below

```bash
scrapy crawl university -o top-us-university.csv
```
