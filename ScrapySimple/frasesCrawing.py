from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class AutorItem(Item):
    nombre = Field()
    lugarNac = Field()


class FrasesCrawler(CrawlSpider):
    name = "PagFrasesCrawl"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+')),
        Rule(LinkExtractor(allow=r'/author'), callback='parse_items'),
    )

    def parse_items(self, response):
        item = ItemLoader(AutorItem(), response)
        item.add_xpath('nombre', '/html/body/div/div[2]/h3/text()')
        item.add_xpath('lugarNac', '/html/body/div/div[2]/p[1]/span[2]/text()')
        yield item.load_item()

# scrapy runspider frasesCrawing.py -o autoresFrases.csv -t csv
