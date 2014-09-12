from django.conf.urls import url,patterns
from todo import views

urlpatterns = patterns(
                       '',
                       url(r'^$',views.index,name="index"),
                       )