from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^authors$', views.authForm),
        url(r'^create_process$', views.creator),
        url(r'^books/(?P<id>\d+)$', views.bookDetail),
        url(r'^authors/(?P<id>\d+)$', views.authDetail),
        url(r'^add_author$', views.additionalAuthor),
        url(r'^add_book$', views.additionalBook),
]