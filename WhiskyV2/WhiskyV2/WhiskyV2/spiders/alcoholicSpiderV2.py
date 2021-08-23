import scrapy
from ..items import Whiskyv2Item
from scrapy.loader import ItemLoader

class AlcoholicSpiderV2(scrapy.Spider):
    name = 'whiskyV2'
    start_urls=['https://www.whiskyshop.com/scotch-whisky']

    def _parse(self, response):
        for products in response.css('div.product-item-info'):
            wv2=ItemLoader(item=Whiskyv2Item(),selector=products)
            wv2.add_css('name','a.product-item-link')
            wv2.add_css('price', 'span.price')
            wv2.add_css('link', 'a.product-item-link::attr(href)')
            yield wv2.load_item()

            siguiente=response.css('a.action.next').attrib['href']
            if siguiente is not None:
                yield response.follow(siguiente,callback=self._parse)