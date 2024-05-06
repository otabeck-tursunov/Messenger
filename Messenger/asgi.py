import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messenger.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

django_asgi_application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
import mainApp.routing

application = ProtocolTypeRouter({
    "http": django_asgi_application,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            mainApp.routing.websocket_urlpatterns
        )
    )
})