from django.apps import AppConfig


class UserAppConfig(AppConfig):

    name = "users"

    def ready(self):
        from users.signals.post_save import post_save_cert_num
