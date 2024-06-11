import scrapy


class CnnSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["www.cnnbrasil.com.br"]
    start_urls = ["https://www.cnnbrasil.com.br/?s=%22intelig%C3%AAncia+artificial%22"]

    def parse(self, response):
        news_names = response.css('h3.news-item-header__title')
        news_date = response.css('span.home__title__date')
        news_url = response.css('li.home__list__item')

        for name,date,url in zip(news_names,news_date,news_url):
            yield {
                'news_title':name.css('h3.news-item-header__title::text').get().strip(),
                'news_date':date.css('span.home__title__date::text').get().strip().split(' ')[0],
                'news_time':date.css('span.home__title__date::text').get().strip().split(' ')[2],
                # 'news_author':,
                'news_url':url.css('li.home__list__item a::attr(href)').get(),
                # 'news_text':,
             }
