from django.apps import AppConfig


class FaqsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "FAQs"
    
    
    def ready(self) -> None:
        import FAQs.signals
