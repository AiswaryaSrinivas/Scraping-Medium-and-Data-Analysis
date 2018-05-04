# Medium Web Scrapper 

To run this, user has to install scrapy library using
pip install scrapy

There are two scrappers
1. medium_scrapper_post.py
This scrapper searches Medium for articles based on a user inputted search string. 

To run the scrapper, use

scrapy runspider -a searchString=searchTerm medium_scrapper_post.py

2. medium_scrapper_tag_archive.py
This scraper get all Articles for a particular tag slug in a given date range

Note : If tag is Data Science, then pass tag as 'data-science' in tagSlug Parameter
To run the scrapper, use


scrapy runspider -a tagSlug='tagSlug' -a start_date=YYYYmmdd -a end_date=YYYYmmdd medium_scrapper_tag_archive.py


# Medium Posts Data Extraction

The file DataExtraction.py extracts information from the json files scrapped by the scrapper medium_scrapper_post.py. 
