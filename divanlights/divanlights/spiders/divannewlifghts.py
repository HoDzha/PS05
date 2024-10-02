import scrapy


class DivannewlifghtsSpider(scrapy.Spider):
    name = "divannewlifghts"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/ufa/category/svet"]

    def parse(self, response):
        pass
