# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EtenderItem(scrapy.Item):
	url1 = scrapy.Field()
    url = scrapy.Field()
    number = scrapy.Field()
    description_short = scrapy.Field()
    category = scrapy.Field()
    date_published = scrapy.Field()
    closing_time_and_date = scrapy.Field()
    compulsory_briefing_session = scrapy.Field()
    free_text = scrapy.Field()
    tender_description = scrapy.Field()
    bid_number = scrapy.Field()
    url2 = scrapy.Field()
    bbbee_points = scrapy.Field()
    directors = scrapy.Field()
    bidder_name = scrapy.Field()
    points_awarded = scrapy.Field()
    participants = scrapy.Field()
    participants_details = scrapy.Field()
    contract_details = scrapy.Field()
    contact_details = scrapy.Field()
    tender_notice = scrapy.Field()
    reason_cancelled = scrapy.Field()



class FileItem(scrapy.Item):
    tender_url = scrapy.Field()
    name = scrapy.Field()
    file_urls = scrapy.Field()
