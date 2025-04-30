from rest_framework.pagination import PageNumberPagination


class TasksPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "task_size"
    max_page_size = 1000

class CategoryPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "category_size"
    max_page_size = 1000

class UserProfilePagination(PageNumberPagination):
    page_size = 5
    page_query_param = "userprofile_size"
    max_page_size = 100

class GroupPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "group_size"
    max_page_size = 100
