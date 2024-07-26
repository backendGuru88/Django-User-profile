from django.apps import AppConfig



class MyAppConfig(AppConfig):
    name = 'app'  # This should match the directory name of your app

    def ready(self):
        import app.signals



class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
