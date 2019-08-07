from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^update_profile/(\d+)',views.update_profile,name='update_profile'),
    url(r'^project/(\d+)',views.new_project,name='project'),
    url(r'^search/', views.search, name='search'),
    url(r'^review/(\d+)',views.reviews,name='reviews'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',views.MerchDescription.as_view()),
    url(r'^api/merch/$', views.ProjectMerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',views.ProjectMerchDescription.as_view()),

    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
