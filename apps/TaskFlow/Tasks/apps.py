from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Tasks"

    def ready(self):
        import Tasks.signals
