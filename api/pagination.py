from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from rest_framework.response import Response
class CustomProductPagination(PageNumberPagination):
    page_size = 4
    def get_paginated_response(self,data):
        return Response({
            "total_products" : self.page.paginator.count,
            "next_page" : self.get_next_link(),
            "previous_page" : self.get_previous_link(),
            "Products" : data
        })

class OrderPagination(CursorPagination):
    page_size = 2
    ordering = '-created_at'