from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='home')

                     ]
