# Third Party Stuff
from rest_framework.routers import DefaultRouter

# xeneta Stuff
from xeneta.base.api.routers import SingletonRouter
from xeneta.portapi.api.views import PortsAPIViewSet
from xeneta.users.api import CurrentUserViewSet
from xeneta.users.auth.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register("auth", AuthViewSet, basename="auth")
singleton_router.register("me", CurrentUserViewSet, basename="me")
default_router.register("ports", PortsAPIViewSet, basename="ports")


# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
