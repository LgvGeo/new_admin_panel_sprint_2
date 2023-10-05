from rest_framework import pagination
from rest_framework.response import Response


class MoviePagination(pagination.PageNumberPagination):
    page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'prev': None if not self.page.has_previous()
            else self.page.previous_page_number(),
            'next': None if not self.page.has_next()
            else self.page.next_page_number(),
            'results': data})
