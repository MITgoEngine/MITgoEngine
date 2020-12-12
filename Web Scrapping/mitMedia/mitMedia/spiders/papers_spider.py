import scrapy
from ..items import MitmediaItem
import json


class PaperSpider(scrapy.Spider):

    with open('D:/MiniProject/Web-Scrapping/mitMedia/urls.json') as f:
        data = json.load(f)
    scrapped_urls = []
    for d in data:
        for url in d["URLS"]:
            scrapped_urls.append(url)

    name = 'papers'
    start_urls = scrapped_urls

    def parse(self, response):

        items = MitmediaItem()          # Container Instance

        # Title of the Publication
        title = response.css('.hero-content-title::text').extract_first()
        # Date of Publication
        date = response.css('.variant-emphasized p::text').extract_first()
        # Author List
        authors = response.css('strong::text').extract()
        # Abstract Paragraphs
        abstract = (response.css(
            '.main-copy p::text').extract())
        abstract = " ".join(abstract)
        # Keywords
        keywords = response.css('.variant-tag-list span::text').extract()
        # Original e-version of the paper
        url = response.css(
            ".publication-link-button::attr('href')").extract_first()
        # Download Link
        download_url = response.css(
            ".file-button::attr('href')").extract_first()
        # Official MIT Link
        official_url = response.url

        items['Title'] = title
        items['Date'] = date
        items['Authors'] = authors
        items['Abstract'] = abstract
        items['Keywords'] = keywords
        items['URL'] = url
        items['DownloadURL'] = download_url
        items['OfficialURL'] = official_url

        yield items
