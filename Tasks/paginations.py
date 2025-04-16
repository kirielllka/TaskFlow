from rest_framework.pagination import PageNumberPagination


class TasksPaginations(PageNumberPagination):
    page_size = 3
    page_query_param = 'task_size'
    max_page_size = 1000

class CategoryPaginations(PageNumberPagination):
    page_size = 3
    page_query_param = 'category_size'
    max_page_size = 1000