from django.apps import AppConfig


class SellPurchaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sell_purchase_app'

    def ready(self):
        import sell_purchase_app.signals  # Import signals module
