import scrapy
from cssutils import parseStyle
import re


class TopicSpider(scrapy.Spider):
    name = 'topic'
    allowed_domains = ['medium.com/topics']
    start_urls = ['http://medium.com/topics/']

    def parse(self, response):
        sections = response.css("div.js-sourceStream > div.streamItem > section")

        for section in sections:
            sc = section.css("header span.heading-title::text").get().strip()
            topics = section.css("div.u-flexColumn.js-sectionItem a.u-backgroundCover")

            for topic in topics:
                tpc = topic.attrib.get("aria-label")
                url = topic.attrib.get("href")
                style = parseStyle(topic.attrib.get("style"))

                img = style['background-image']
                img = re.search('url\((.*)\)', img)[1]

                yield {
                    'topic': tpc,
                    'url': url,
                    'section': sc,
                    'image': img
                }
