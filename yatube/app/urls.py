from app import views as app_views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', app_views.sample_view),
]
