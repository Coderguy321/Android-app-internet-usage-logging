from django.conf.urls import url
# from .views import SngcVisualisationView, CurrentDateView, TotalTimeView,\
#     WeeklyView, MostUsedView, LeastUsedView, Last7DaysView, MostUsedAllUsersView, MinUsedAllUsersView, \
#     ActiveUsersLast7View
from .views import CameraView, StatusView

urlpatterns = [
    url(r'alert/', CameraView.as_view()),
    url(r'status/', StatusView.as_view()),
    # url(r'current_date', CurrentDateView.as_view()),
    # url(r'total_time_most_used_10apps', TotalTimeView.as_view()),
]