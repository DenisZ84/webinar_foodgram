from rest_framework.pagination import PageNumberPagination

from foodgram.contants import PAGE_SIZE


class CustomPageNumberPagination(PageNumberPagination):
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'