from django.conf.urls import url, include
from apps.adopcion.views import index_adopcion

urlpatterns = [
    url(r'^$', index_adopcion),
]
