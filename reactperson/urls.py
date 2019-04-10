from django.conf.urls import url
from reactperson import views

urlpatterns = [
    url(r'^register$', views.register.as_view(), name='register'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^$', views.index.as_view(), name='index'),
    url(r'zjp', views.api.as_view(), name='api'),

    '''
    url(r'^goods/(?P<goods_id>\d+)$', views.DetailView.as_view(), name='detail'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', views.ListView.as_view(), name='detail'),

    '''
]
