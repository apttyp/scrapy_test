import scrapy

class QtSpider(scrapy.Spider):
    name = "quotes"
    #example1
	# def start_requests(self):
	# 	urls = [
 #            'http://quotes.toscrape.com/page/1/',
 #            'http://quotes.toscrape.com/page/2/',
	# 	]
	# 	for url in urls:
	# 		yield scrapy.Request(url=url, callback=self.parse)

	# def parse(self, response):
	# 	page=response.url.split("/")[-2]
	# 	filename='quotes-%s.html' % page
	# 	with open(filename,'wb') as f:
	# 		f.write(response.body)
	# 	self.log('Saved file %s' % filename)
        
    # example2
	# start_urls = [
 #        'http://quotes.toscrape.com/page/1/',
 #        'http://quotes.toscrape.com/page/2/',
	# ]

	# def parse(self, response):
	# 	self.log("=========================")
	# 	for item in response.xpath('//div[@class="quote"]'):
	# 	    yield{
 #                'text':item.xpath('span[text()]').extract_first(),
 #                'author':item.xpath('span/small[text()]').extract_first(),
 #                'tags':item.xpath('div/a[text()]').extract_first(),
	# 	    }
    #example3
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    # ]
    # def parse(self,response):
    #     for item in response.xpath('//div[@class="quote"]'):
    #         yield {
    #             'text':item.xpath('span[text()]').extract_first(),
    #             'author':item.xpath('span/small[text()]').extract_first(),
    #             'tags':item.xpath('div/a[text()]').extract_first(),
    #         }
    #     next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         self.log(next_page)
    #         yield scrapy.Request(next_page,callback=self.parse)

    #example4
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for item in response.xpath('//div[@class="quote"]'):
            yield {
                'text':item.xpath('span/text()').extract_first(),
                'author':item.xpath('span/small/text()').extract_first(),
                'tags':item.xpath('div/a/text()').extract_first(),
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            self.log('next_page is :%s' % next_page)
            # log.msg('next_page is : %s' % next_page, level=log.INFO)
            yield response.follow(next_page, callback=self.parse)
