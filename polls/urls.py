from django.conf.urls import url




from . import views

app_name = 'polls'
urlpatterns = [
               url(r'^$', views.IndexView.as_view(), name='index'),
               url(r'^produit/$', views.produitView.as_view(), name='produit'),

               url(r'^produit/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
               
               url(r'^windsurf/$', views.windsurfView.as_view(), name='windsurf'),

               url(r'^windsurf/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
               #url(r'^list/', views.SlideView.as_view()),
               #url(r'^$', views.SlideView.as_view(), name='slide'),
               #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
               ]









"""
url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
"""