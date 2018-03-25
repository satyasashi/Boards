from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^boards/(?P<pk>\d+)/$', views.board_topic, name="board_topic"),
    url(r'^admin/', admin.site.urls),
]
