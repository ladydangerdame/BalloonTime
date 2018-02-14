from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.party_list, name='party_list'),
    url(r'(?P<pk>\d+)/$', views.party_detail),
    url(r'^party_create/$', views.PartyCreate.as_view(), name="party_create"),
    url(r'^party/(?P<pk>[0-9]+)/$', views.PartyUpdate.as_view(), name='party_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.PartyDelete.as_view(), name='party_delete'),

]
