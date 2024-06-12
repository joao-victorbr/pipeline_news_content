### Summary:
This repository is the result of a data engineering challenge. The instructions and objectives of the challenge follow in the last topic of this README.
Data collection was carried out through a search for "artificial intelligence" in news on the CNN Brasil website.
The collection and processing results are stored in a json file.
This is just the beginning of the pipeline, because I couldn't do the rest of the project in time and study/research for it.

### Execution:
After cloning the repository in a local environment, enter the "pipeline_news_content_news_content_collect" folder. Then run the command below:
``scrapy crawl cnn -o data_extract/teste.json``

At this moment, a json file is created in the "news_content_content_collect/data_extract" folder with all the news present on the first search page of the CNN's site.

### Challenge instructions:
#### Challenge - News Content Collect and Store
Create a solution that crawls for articles from a news website, cleanses the response, stores in BigQuery (bonus) then makes it available to search via an API.

#### Details
Write an application to crawl an online news website, e.g. www.theguardian.com/au or www.bbc.com using a crawler framework such as [Scrapy] (http://scrapy.org/). You can use a crawl framework of your choice and build the application in Python.
The appliction should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html
Store the data in BigQuery, for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original.

#### Bonus
Write an API that provides access to the content in BigQuery database. The user should be able to search for articles by keyword