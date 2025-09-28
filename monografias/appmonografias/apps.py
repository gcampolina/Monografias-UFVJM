from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appmonografias'

    def ready(self):
        # Importa signals quando a app é inicializada
        import appmonografias.signals