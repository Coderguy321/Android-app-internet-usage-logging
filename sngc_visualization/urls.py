from django.conf.urls import url
from .views import SngcVisualisationView, get_data_user0, get_data_user1, get_data_user2
urlpatterns = [
    url(r'^$', SngcVisualisationView.as_view()),
    url(r'^wxeCwqgggi$', get_data_user1),
    url(r'^10t8YFlPCg$', get_data_user0),
    url(r'^nxGETSeYPk$', get_data_user2)
]