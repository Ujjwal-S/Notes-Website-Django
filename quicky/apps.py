from django.apps import AppConfig


class QuickyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quicky'

    def ready(self):
        import quicky.signals
