import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.xpath('//span/a[text()="(about)"]/@href'):
            yield response.follow(href, self.parse_author)
        for href in response.xpath('//li[@class="next"]/a[@href]'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_xpath(query):
        	return response.xpath(query).extract_first().strip()

        yield{
            'name': extract_with_xpath('//h3/text()'),
            'birthdate': extract_with_xpath('//span[@class="author-born-date"]/text()'),
            'bio': extract_with_xpath('//div[@class="author-description"]/text()'),
        }

    def closed(self, reason):# 爬取结束的时候发送邮件  
        from scrapy.mail import MailSender  
  
        mailer = MailSender(  
            smtphost = "smtp.163.com",  # 发送邮件的服务器  
            mailfrom = "hahahaha",   # 邮件发送者  
            smtpuser = "123@163.com",   # 用户名  
            smtppass = "***",  # 发送邮箱的密码不是你注册时的密码，而是授权码！！！切记！  
            smtpport = 25   # 端口号  
        )  

        # 如果说发送的内容太过简单的话，很可能会被当做垃圾邮件给禁止发送。  
        mailer.send(to=["tonystark@aispeech.com"], subject='我是主题', body='发送的邮件内容')
