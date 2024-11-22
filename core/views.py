from django.db.models import Q
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from .models import BooksBook
from .serializers import BooksBookSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 25 
    page_size_query_param = 'page_size'  
    max_page_size = 100 


class BooksBookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BooksBook.objects.all().prefetch_related(
        'booksbookauthors_set', 
        'booksbooklanguages_set', 
        'booksbooksubjects_set', 
        'booksbookbookshelves_set', 
        'booksformat_set'
    )
    serializer_class = BooksBookSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        search_query = request.query_params.get('search', '')
        query = Q()

        if search_query:
            # Searching across multiple fields using Q objects
            query &= Q(title__icontains=search_query) | \
                     Q(booksbookauthors__author__name__icontains=search_query) | \
                     Q(booksbooklanguages__language__code__icontains=search_query) | \
                     Q(booksbooksubjects__subject__name__icontains=search_query) | \
                     Q(booksbookbookshelves__bookshelf__name__icontains=search_query)

        # Filter the queryset based on the query
        queryset = self.get_queryset().filter(query)

        # Get the total count of matching books
        total_count = queryset.count()

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'count': total_count,
                'results': serializer.data
            })

        # If no pagination, return all data (in case pagination is not needed)
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': total_count,
            'results': serializer.data
        })
