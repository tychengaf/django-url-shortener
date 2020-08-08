from django.contrib import admin
from django.urls import path
from core.views import HomePageView, ShortenUrlView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('<slug:shorten_hash>/', ShortenUrlView.as_view(), name="shorten-hash")
]
