import requests
from django.core import serializers


class SearchAddres:

    def __init__(self):

        self.confirm_key = "TESTJUSOGOKR"
        self.current_page = 1
        self.count_per_page = 10
        self.request_url = "http://www.juso.go.kr/addrlink/addrLinkApiJsonp.do"

    def set_keyword(self, keyword):

        self.keyword = keyword

    def set_page(self, page):

        self.current_page = page

    def get_page(self):

        return self.current_page

    def request_address_search(self, keyword, page):

        response_as_json = self.request_url.post(
                self.request_url,
                data={
                    'confmKey': self.confirm_key,
                    'currentPage': self.current_page,
                    'countPerPage':  self.count_per_page,
                    'keyword': keyword,
                }
        )
