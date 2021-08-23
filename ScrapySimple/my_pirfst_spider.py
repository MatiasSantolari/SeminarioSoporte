from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


# Problema: Extraer informacion de StackOverflow: Preguntas

class Pregunta(Item):
    pregunta = Field()
    id = Field()


class StackOverflowSpider(Spider):
    name = "MiPrimerSpider"
    start_urls = ['https://es.stackoverflow.com/']

    def parse(self, response, **kwargs):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="question-mini-list"]/div')

        # Iterar sobre todas las preguntas
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_value('id', i)
            yield item.load_item()

# scrapy runspider my_pirfst_spider.py -o preguntasSOF.csv -t csv
