from django.apps import AppConfig
# import signals


class RegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'register'

    def ready(self):
        print("ready called")
        from . import signals
#
# class UsersConfig(AppConfig):
#     name = 'register'



# default_app_config = 'register.apps.UsersConfig'
