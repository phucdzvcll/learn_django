from django.apps import AppConfig


class TestNewAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_new_app'
