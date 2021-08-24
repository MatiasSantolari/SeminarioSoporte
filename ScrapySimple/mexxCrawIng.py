from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class MexxItem(Item):
    nombre = Field()
    precio = Field()


class MexxCrawler(CrawlSpider):
    name = "MiPrimerCrawl"
    allowed_domains = ['mexx.com.ar']
    start_urls = ['https://www.mexx.com.ar/productos-rubro/gabinetes/']

    rules = (
        Rule(LinkExtractor(allow=r'/?pagina=')),
        Rule(LinkExtractor(allow=r'mid-tower'), callback='parse_items'),
    )

    def parse_items(self, response):
        item = ItemLoader(MexxItem(), response)
        item.add_xpath('nombre', '//*[@id="prod_desc_edit"]/h2[1]/text()')
        item.add_xpath('precio', '//*[@id="prod_desc_edit"]/h2[2]/b[2]/text()')
        yield item.load_item()

#scrapy runspider mexxCrawIng.py -o mexx.csv -t csv
