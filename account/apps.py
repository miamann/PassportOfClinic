from django.apps import AppConfig


class AccountConfig(AppConfig):
    name ='account'

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

