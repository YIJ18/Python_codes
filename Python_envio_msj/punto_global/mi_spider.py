import scrapy

class MiSpider(scrapy.Spider):
    name = "mi_spider"
    start_urls = ['https://www.hackerone.com/']

    def parse(self, response):
        for titulo in response.css('h2::text'):
            yield {'titulo': titulo.get()}

        for link in response.css('a::attr(href)'):
            yield response.follow(link, self.parse)
