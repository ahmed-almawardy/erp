from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PaymentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payment'
    verbose_name = _('Payment')
    
    def ready(self) -> None:
        import payment.signals