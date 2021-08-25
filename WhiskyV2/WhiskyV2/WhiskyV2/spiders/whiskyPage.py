import scrapy
from ..items import Whiskyv2Item
from scrapy.loader import ItemLoader


class wSpider(scrapy.Spider):
    name = 'whiskyV3'
    #allowed_domains = ['whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/scotch-whisky',
                  'https://www.whiskyshop.com/spirits',
                  'https://www.whiskyshop.com/world-whiskies']

    def _parse(self, response):
        category = response.css('span.base::text').get()
        webpage = response.url
        for products in response.css('div.product-item-info'):
            wv2 = ItemLoader(item=Whiskyv2Item(), selector=products)
            wv2.add_css('name', 'a.product-item-link')
            wv2.add_css('price', 'span.price')
            wv2.add_value('category', category)
            wv2.add_css('link', 'a.product-item-link::attr(href)')
            wv2.add_value('listed', webpage)
            yield wv2.load_item()
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
            try:
                siguiente = response.css('a.action.next').attrib['href']
                if siguiente is not None:
                    yield response.follow(siguiente, callback=self._parse)
<<<<<<< Updated upstream
            except Exception:
                pass  # esta excepcion se genera porque no encuetra el boton de pagina siguiente que se esta asignando
=======
            except Exception as e:
                if 'https://www.whiskyshop.com/spirits' not in response.url:
                    yield response.follow('https://www.whiskyshop.com/spirits', callback=self._parse)
                else:
                    yield response.follow('https://www.whiskyshop.com/world-whiskies', callback=self._parse)
>>>>>>> Stashed changes
