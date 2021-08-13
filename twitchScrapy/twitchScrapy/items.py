# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitchscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #info de categorias
    titulo=scrapy.Field()
    cant_espectadores_global=scrapy.Field()
    cant_seguidores_global=scrapy.Field()

