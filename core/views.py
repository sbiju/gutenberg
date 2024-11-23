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
        gutenberg_id = request.query_params.get('id', None)
        language = request.query_params.get('language', None)
        mime_type = request.query_params.get('mime_type', None)
        topic = request.query_params.get('topic', None)
        author = request.query_params.get('author', None)
        title = request.query_params.get('title', None)

        query = Q()

        if gutenberg_id:
            query &= Q(gutenberg_id=gutenberg_id)

        if language:
            query &= Q(booksbooklanguages__language__code__iexact=language)

        if mime_type:
            query &= Q(booksformat__mime_type__iexact=mime_type)

        if topic:
            query &= Q(booksbooksubjects__subject__name__icontains=topic) | \
                    Q(booksbookbookshelves__bookshelf__name__icontains=topic)

        if author:
            query &= Q(booksbookauthors__author__name__icontains=author)

        if title:
            query &= Q(title__icontains=title)

        queryset = self.get_queryset().filter(query).order_by('-download_count').distinct()

        total_count = queryset.count()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'count': total_count,
                'results': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': total_count,
            'results': serializer.data
        })
