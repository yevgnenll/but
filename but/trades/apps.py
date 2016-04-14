from django.apps import AppConfig


class AppConfigTrade(AppConfig):

    name = "trades"

    def ready(self):
        from trades.signals.post_save import post_save_hashid
