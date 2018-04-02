import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = respone.url.split('/')[-2]
        filename = 'quotes-{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
