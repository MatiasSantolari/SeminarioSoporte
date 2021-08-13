import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from items import TwitchscrapyItem


class SpiderRat(CrawlSpider):
    name = "spiderRat"
    item_count=0
    allowed_domain=['https://www.twitch.tv/']
    start_urls = [
        'https://www.twitch.tv/directory'
    ]
    rules = {
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[@class="Layout-sc-nxg1ff-0 cCZECl"]')),
             callback='parse_item',follow=False)

    }
    def parse_item(self, response):
        rat=TwitchscrapyItem()

        #info de la categoria
        rat['titulo'] = response.xpath('//h1[@class="CoreText-sc-cpl358-0 ScTitleText-sc-1gsen4-0 gAYdrP tw-title"]/text()').extract()
        rat['cant_espectadores_global'] = response.xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/p/strong/text()').extract()
        rat['cant_seguidores_global'] = response.xpath('//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/p/strong/text()').extract()
        self.item_count +=1
        if self.item_count>10:
            raise CloseSpider('item_exceeded')
        yield rat

