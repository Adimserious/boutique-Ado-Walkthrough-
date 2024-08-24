from django.apps import AppConfig

# the ready method is overridden by importing sgnal method

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals