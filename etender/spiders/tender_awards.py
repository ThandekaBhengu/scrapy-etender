# -*- coding: utf-8 -*-
import scrapy
from etender.items import EtenderItem, FileItem
import html2text


class TendersSpider(scrapy.Spider):
    name = 'awards'
    allowed_domains = ['etenders.treasury.gov.za']
    start_urls = ['https://etenders.treasury.gov.za/content/awarded-tenders']

    def parse(self, response):
        some_tender_row_title = response.css('td.views-field-title')[0]
        tender_table = some_tender_row_title.xpath('../..')
        for tender_row in tender_table.xpath('tr'):
            url1 = tender_row.css('td.views-field-title a::attr(href)').get()

            meta = {
                'url1': url1,
                'category': tender_row.css('td.views-field-field-tender-category::text').get().strip(),
                'tender_description': tender_row.css('td.views-field-title a::text').get().strip(),
                'bid_number': tender_row.css('td.views-field-field-code::text').get().strip(),
            }
            yield scrapy.Request(response.urljoin(url1),
                                 callback=self.parse_layer_2,
                                 meta=meta
                                 )
        next_page = response.css('li.pager-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_layer_2(self, response):
        url2 = response.css('td.views-field-field-successful-bidder a::attr(href)').get()
        meta = response.meta
        meta['bidder_name'] = response.css('td.views-field-field-successful-bidder a::text').get().strip(),
        meta['bbbee_points'] = response.css('td.views-field-field-bbbee-points::text').get().strip(),
        meta['points_awarded'] = response.css('td.views-field-field-point-awarded::text').get().strip(),
        meta['participants'] = response.css('td.views-field-field-participant::text').get().strip(),
        meta['participants_details'] = response.css('td.views-field-field-participants-contact-detai').get().strip(),

        yield scrapy.Request(response.urljoin(url2),
                             callback=self.parse_tender,
                             meta=meta
                             )

        next_page = response.css('li.pager-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_tender(self, response):
        etender = EtenderItem()
        etender['url2'] = response.url
        etender['url1'] = response.meta['url1']
        etender['category'] = response.meta['category']
        etender['tender_description'] = response.meta['tender_description']
        etender['bid_number'] = response.meta['bid_number']
        etender['bidder_name'] = response.meta['bidder_name']
        etender['bbbee_points'] = response.meta['bbbee_points']
        etender['points_awarded'] = response.meta['points_awarded']
        etender['participants'] = response.meta['participants']
        etender['participants_details'] = response.meta['participants_details']
        etender['directors'] = response.css('div.field-name-field-directors').get()
        etender['contract_details'] = response.css('div.field-name-field-contract-detail').get()
        etender['contact_details'] = response.css('div.field-name-field-contact-details').get()

        yield etender
