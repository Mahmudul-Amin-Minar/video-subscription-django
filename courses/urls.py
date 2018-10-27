from django.conf.urls import url

from .views import CourseListView, CourseDetailView, LessonDetailView

app_name = 'courses'

urlpatterns = [
    url(r'^$', CourseListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<course_slug>[\w-]+)/(?P<lesson_slug>[\w-]+)/$', LessonDetailView.as_view(), name='lesson_detail'),
]
