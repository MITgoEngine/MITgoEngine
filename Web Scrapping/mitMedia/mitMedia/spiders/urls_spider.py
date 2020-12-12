import scrapy
from ..items import MitmediaItem


class PaperSpider(scrapy.Spider):

    # Create the scrapable urls from urls.json
    scrapable_urls = []
    for i in range(7):
        scrapable_urls.append(
            "https://www.media.mit.edu/search/?page="+str(i+1)+"&filter=publication")

    name = 'urls'
    start_urls = scrapable_urls

    def parse(self, response):

        URLS = response.css(".listing-layout-item::attr('data-href')").extract()
        for i in range(len(URLS)):
            URLS[i] = "https://www.media.mit.edu" + URLS[i]
        yield {
            'URLS': URLS
        }
