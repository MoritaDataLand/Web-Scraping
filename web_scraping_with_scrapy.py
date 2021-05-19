import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls=["http://quotes.toscrape.com/"]

    def parse(self, response):
        for item in response.css("div.quote"):
            yield{
                "text" :item.css("span.text::text").get(),
                "author" : item.css("small.author::text").get(),
                "tags" : item.css("div.tags a.tag::text").getall()
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)