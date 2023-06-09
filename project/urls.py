from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from myapp.views import *
urlpatterns = [
    path('i18n/',include('django.conf.urls.i18n')),
    path("set_language/<str:language>", set_language, name="set-language"),
]
urlpatterns += i18n_patterns(
    path('api/',include('myapp.urls')),
    path('', admin.site.urls),
    
)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)