# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from .settings import UAPOOLS

class UserAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.user_agent = UAPOOLS

    def process_request(self,request,spider):
        UA = random.choice(self.user_agent)
        request.headers['User-Agent'] = UA
        print("==============UA===============% s" % UA)