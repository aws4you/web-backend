from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contactmanager import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'topics', views.TopicViewSet)
router.register(r'webpages', views.WebPageViewSet)
router.register(r'accessrecords', views.AccessRecordViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
