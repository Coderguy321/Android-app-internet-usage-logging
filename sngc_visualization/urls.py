from django.conf.urls import url
from .views import SngcVisualisationView, CurrentDateView, TotalTimeView,\
    WeeklyView, MostUsedView, LeastUsedView, Last7DaysView, MostUsedAllUsersView, MinUsedAllUsersView
urlpatterns = [
    url(r'^$', SngcVisualisationView.as_view()),
    url(r'current_date', CurrentDateView.as_view()),
    url(r'total_time_most_used', TotalTimeView.as_view()),
    url(r'weekly_time_used', WeeklyView.as_view()),
    url(r'most_used', MostUsedView.as_view()),
    url(r'least_used', LeastUsedView.as_view()),
    url(r'last7_days', Last7DaysView.as_view()),
    url(r'max_used_all', MostUsedAllUsersView.as_view()),
    url(r'min_used_all', MinUsedAllUsersView.as_view()),
]