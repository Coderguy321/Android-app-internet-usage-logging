from django.conf.urls import url
from .views import SngcVisualisationView
urlpatterns = [
    url(r'^$', SngcVisualisationView.as_view())
]