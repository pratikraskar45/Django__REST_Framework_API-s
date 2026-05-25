# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response


# class CustomPagination(PageNumberPagination):
    
#     page_size_query_param='page_size'
    
#     page_query_param='ppage_size'
#     max_page_size=10
    
    
#     def get_paginated_response(self, data):
#         return Response(
#             {
#                 'next':self.get_next_link(),
#                 'previous':self.get_previous_link(),
#                 'count':self.page.paginator.count,
#                 'page_size':self.page_size,
#                 'result':data
#             }
#         )
        
        
        
# if pagination and filter not use one time then use below code
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):

    page_size = 2

    page_query_param = 'page'

    page_size_query_param = 'page_size'

    max_page_size = 10

    def get_paginated_response(self, data):

        return Response({

            'count': self.page.paginator.count,

            'next': self.get_next_link(),

            'previous': self.get_previous_link(),

            'results': data

        })