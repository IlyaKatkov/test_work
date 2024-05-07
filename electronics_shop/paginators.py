from rest_framework.pagination import PageNumberPagination


class SupplierPaginator(PageNumberPagination):
    """ Пагинация для вывода списка поставщиков."""
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100