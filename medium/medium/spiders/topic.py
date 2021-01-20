import scrapy


class TopicSpider(scrapy.Spider):
    name = 'topic'
    allowed_domains = ['medium.com/topics']
    start_urls = ['http://medium.com/topics/']

    def parse(self, response):
        pass
