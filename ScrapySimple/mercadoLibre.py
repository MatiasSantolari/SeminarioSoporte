from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor


class Articulo(Item):
    titulo = Field()
    precio = Field()


class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 80
    }
    download_delay = 1

    allowed_domains = ['celulares.mercadolibre.com.ar', 'mercadolibre.com.ar']
    # puedo poner más dominios solo poniendo comas

    start_urls = ['https://celulares.mercadolibre.com.ar/']

    rules = (
        Rule(  # REGLA #1 => HORIZONTALIDAD POR PAGINACION
            LinkExtractor(allow=r'/_Desde_\d+'), follow=True),

        Rule(  # REGLA #2 => VERTICALIDAD AL DETALLE PRODUCTOS
            LinkExtractor(allow=r'pdp_filters=category:MLA1055#searchVariation=MLA'),
            follow=True, callback='parse_items'),
    )

    def parse_items(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo', '//*[@id="root-app"]/div[2]/div[2]/'
                                 'div[1]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/h1/text()')
        item.add_xpath('precio', '//*[@id="root-app"]/div[2]/div[2]/'
                                 'div[1]/div[1]/div/div[1]/div[2]/div[3]/div[1]/span[1]/span[1]/text()')
        yield item.load_item()

# scrapy runspider mercadoLibre.py -o celularesML.csv -t csv
