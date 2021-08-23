import scrapy

class AlcoholicSpider(scrapy.Spider):
    name = 'whisky'
    start_urls=['https://www.whiskyshop.com/scotch-whisky']

    def _parse(self, response):
        for products in response.css('div.product-item-info'):
            try:
                yield {
                    'nombre':products.css('a.product-item-link::text').get(),
                    'precio':products.css('span.price::text').get(),
                    'link':products.css('a.product-item-link').attrib['href'],
                }
            except Exception as e:
                yield {
                    'nombre': products.css('a.product-item-link::text').get(),
                    'precio': 'Agotado',
                    'link': products.css('a.product-item-link').attrib['href'],
                }

            siguiente = response.css('a.action.next').attrib['href']
            if siguiente is not None:
                yield response.follow(siguiente, callback=self._parse)