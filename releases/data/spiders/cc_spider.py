from pathlib import Path

import scrapy
from ..constants.constants import *

class PtReleasesSpider(scrapy.Spider):
    name = "cc"

    COUNT_MAX = 3
    count = 0

    def start_requests(self):
        url = "https://comunidadeculturaearte.com/category/artigos/criticas/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get every row
        rows = response.css(".row-flex")
        for row in rows:
            # check category and filter reviews only
            category = row.css(".tag-categoria a::text").get()
            review_page = row.css(".p1 .bt ::attr(href)").get()

            if category.lower() == "críticas" and review_page is not None:
                    # go to each review's page and parse
                    yield scrapy.Request(review_page, callback=self.parse_review)

        self.count += 1
        if (self.count < self.COUNT_MAX):
            pagination_link = response.css(".next ::attr(href)").get()
            yield scrapy.Request(pagination_link, callback=self.parse)
                    
    def parse_review(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        category = extract_with_css(".post-categories li:nth-child(2) a::text")  
        if (category == CC_MUSIC_TAG):
            yield {
               "autor" : extract_with_css(".pb-3 a::text")
            }